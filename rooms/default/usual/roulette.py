from localizations import locale_manager
from constants import *
import random
import databasemanager

name = 'Казино "Марианская Впадина"'

actions_enter = [ locale_manager.get('rooms.default.usual.roulette.phrase_4'), locale_manager.get('rooms.default.usual.roulette.phrase_5') ]
actions_choose = [ 'Красное x2', 'Зеленое x12', 'Черное x2' ]
actions_make_bet = [ '100', '250', '500', '1000', locale_manager.get('rooms.default.usual.roulette.phrase_6') ]


def can_open(user, reply):
	return not user.has_tag(DEVIL)

def open_failure(user, reply):
	reply(locale_manager.get('rooms.default.usual.roulette.phrase_7'))

def enter(user, reply):
	msg = (
		locale_manager.get('rooms.default.usual.roulette.phrase_1'))

	user.set_room_temp('gold', user.gold)

	reply(msg, photo=CASINO_STICKER)


def get_actions(user):
	question = user.get_room_temp('question', def_val='enter')

	switcher = {
		'enter': actions_enter,
		'choose': actions_choose,
		'make_bet': actions_make_bet
	}

	actions = switcher.get(question)

	return actions


def action(user, reply, text):
	question = user.get_room_temp('question', def_val='enter')

	switcher = {
		'enter': action_enter,
		'choose': action_choose,
		'make_bet': action_make_bet
	}

	func = switcher.get(question)

	return func(user, reply, text)


def action_enter(user, reply, text):
	if text not in actions_enter:
		msg = (
			locale_manager.get('rooms.default.usual.roulette.phrase_8')
		)

		reply(msg)

		return

	if text == actions_enter[1]:
		msg = (
			' — Азартные игры не для меня, — подумал ты и ушел в коридор'
		)

		reply(msg)

		gold = user.get_room_temp('gold')

		if user.gold > gold:
			msg = (
				locale_manager.get('rooms.default.usual.roulette.phrase_9')
			)

			reply(msg.format(user.gold - gold))

		if user.gold < gold:
			msg = (
				locale_manager.get('rooms.default.usual.roulette.phrase_10')
			)

			databasemanager.add_to_leaderboard(user, gold - user.gold, databasemanager.ROULETTE_TABLE)

			reply(msg.format(gold - user.gold))

		user.leave(reply)

		return

	msg = (
		' - Ну чтож, выбирайте ставки, Господа!, — диллер посмотрел на тебя с ухмылкой'
	)

	reply(msg)

	user.set_room_temp('question', 'choose')


def action_choose(user, reply, text):
	if text not in actions_choose:
		msg = (
			locale_manager.get('rooms.default.usual.roulette.phrase_11')
		)

		reply(msg)

		return

	switcher = {
		actions_choose[0]: 'red',
		actions_choose[1]: 'zero',
		actions_choose[2]: 'black'
	}

	choose = switcher.get(text)
	
	user.set_room_temp('color', choose)

	msg = (
		' — Твой выбор {}. Какова же твоя ставка?'
	)

	reply(msg.format(text))

	user.set_room_temp('question', 'make_bet')


def action_make_bet(user, reply, text):
	bet = 0

	if text == actions_make_bet[4]:
		msg = (
			locale_manager.get('rooms.default.usual.roulette.phrase_12')
		)

		reply(msg)

		user.set_room_temp('question', 'enter')

		return

	try:
		bet = int(text)
	except:
		reply(locale_manager.get('rooms.default.usual.roulette.phrase_13'))

		return

	if bet <= 0:
		msg = (
			' — Что ты мямлишь? Говори четче!, — сказал тебе диллер'
		)

		reply(msg)

		return

	if not user.paid(bet):
		msg = (
			locale_manager.get('rooms.default.usual.roulette.phrase_14')
		)

		reply(msg)

		return

	msg = (
		locale_manager.get('rooms.default.usual.roulette.phrase_2'))

	reply(msg.format(user.name, bet))


	msg = (
		locale_manager.get('rooms.default.usual.roulette.phrase_15')
	)

	number = get_random_number()
	color = get_color(number)

	switcher = {
		'red': actions_choose[0],
		'zero': actions_choose[1],
		'black': actions_choose[2]
	}

	color_text = switcher.get(color)

	reply(msg.format(number, color_text))


	user_color = user.get_room_temp('color')

	if color == user_color:
		msg = (
			locale_manager.get('rooms.default.usual.roulette.phrase_3'))

		coins = 0

		if color in ['red', 'black']:
			coins = bet
		else:
			coins = bet * 12

		reply(msg.format(coins))

		user.give_gold(coins + bet)

	else:
		msg = (
			' — Сегодня удача не на твоей стороне, дружище!'
		)

		reply(msg)

	user.set_room_temp('question', 'enter')


def get_random_number(min = 0, max = 12):

	return random.randrange(min, max + 1, 1)


def get_color(number):
	if number == 0:
		return 'zero'
	elif number % 2:
		return 'black'
	else:
		return 'red'
