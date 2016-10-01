from constants import *
import random
import databasemanager

name = 'Казино "Марианская Впадина"'

actions_enter = [ 'Играем', 'Уйти' ]
actions_choose = [ 'Красное x2', 'Зеленое x12', 'Черное x2' ]
actions_make_bet = [ '100', '250', '500', '1000', 'Назад' ]


def can_open(user, reply):
	return not user.has_tag(DEVIL)

def open_failure(user, reply):
	reply('Здесь не рады проклятым!')

def enter(user, reply):
	msg = (
		'Ты вошел в комнату и увидел множество игральных столов.\n'
		'Диллер, стоящий за одним из столов, зазывает тебя:\n'
		' — Ну что, играть будем?'
	)

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
			'Что-то?'
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
				'Ты в плюсе на {}'
			)

			reply(msg.format(user.gold - gold))

		if user.gold < gold:
			msg = (
				'Ты в минусе на {}'
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
			'Определись с выбором!'
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
			'Слабак!'
		)

		reply(msg)

		user.set_room_temp('question', 'enter')

		return

	try:
		bet = int(text)
	except:
		reply('Непонятное число у вас.')

		return

	if bet <= 0:
		msg = (
			' — Что ты мямлишь? Говори четче!, — сказал тебе диллер'
		)

		reply(msg)

		return

	if not user.paid(bet):
		msg = (
			'У тебя нет столько денег.'
		)

		reply(msg)

		return

	msg = (
		'Игрок {} делает ставку {}. '
		'Ставки сделаны, игра начинается!'
	)

	reply(msg.format(user.name, bet))


	msg = (
		'На рулетке выпадает {} - {}'
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
			' — Ограбить казино собрался? Держи свои {}\n'
			'   Посмотрим повезет ли тебе в следующий раз..'
		)

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
