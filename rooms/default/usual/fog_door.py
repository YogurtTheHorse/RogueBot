from constants import *
import bossmanager
import random

name = 'Темная комната'

actions_enter =  [ 'Пойти дальше', 'Уйти' ]
actions_try_to_see = [ 'Посмотреть сквозь туман', 'Развернуться и уйти' ]
actions_pass_throw_fog = [ 'Пройти сквозь туман', 'Убежать прочь' ]

def can_open(user, reply):
	return not user.has_tag(DEVIL)

def open_failure(user, reply):
	reply('Здесь не рады проклятым!')

def enter(user, reply):
	msg = (
		'Ты вошел в комнату и почувствовал запах прогнившей плоти.\n'
		' — Что это за запах?, — подумал ты'
	)

	reply(msg, photo=FOG_STICKER)


def get_actions(user):
	question = user.get_room_temp('question', def_val='enter')

	switcher = {
		'enter': actions_enter,
		'try_to_see': actions_try_to_see,
		'pass_throw_fog': actions_pass_throw_fog
	}

	actions = switcher.get(question)

	return actions


def action(user, reply, text):
	question = user.get_room_temp('question', def_val='enter')

	switcher = {
		'enter': action_enter,
		'try_to_see': action_try_to_see,
		'pass_throw_fog': action_pass_throw_fog
	}

	func = switcher.get(question)

	return func(user, reply, text)


def action_enter(user, reply, text):
	if text == actions_enter[0]:
		msg = (
			'Ты продолжил путь, и через мгновенье перед тобой оказались огромные врата, наполненные туманом.\n'
			' — Где-то я это уже видел, — подумалось тебе.\n'
		)

		reply(msg)

		user.set_room_temp('question', 'try_to_see')

	else:
		msg = (
			'Ты не стал продолжать путь, вышел из комнаты, и так и не узнал что в ней было.'
		)

		reply(msg)

		user.leave(reply)


def action_try_to_see(user, reply, text):
	if text == actions_try_to_see[0]:
		boss = bossmanager.current()

		if boss['alive']:
			msg = (
				'Ты подошел ближе к туману, но ничего не увидел.\n'
				'Однако ты услышал рыки злобного чудища и крики людей.\n'
			)

			reply(msg)

			user.set_room_temp('question', 'pass_throw_fog')

		else:
			msg = (
				'Подойдя ближе, туман рассеялся, и за ним ты увидел гору трупов.\n'
				'Может быть к счастью?'
			)

			reply(msg)

			user.leave(reply)

	else:
		msg = (
			'Ты так и не узнал что находится за туманом и ушел.'
		)

		reply(msg)

		user.leave(reply)


def action_pass_throw_fog(user, reply, text):
	if text == actions_pass_throw_fog[0]:
		msg = (
			'Пройдя сквозь туман ты увидел множество людей таких как ты и ...\n'
			'...\n'
			'...\n'
			'...'
		)

		reply(msg)

		boss = bossmanager.current()

		user.open_room(reply, 'boss', boss['name'])

	else:
		random_number = random.random()

		if random_number < 0.2:
			msg = (
				'Когда ты убегал из комнаты, ты вовремя заметил лежащий камень на земле и успел увернуться.'
			)

			reply(msg)

		else:
			msg = (
				'Ты убегал настолько быстро, что не заметил лежащий на земле камень и споткнулся об него.'
			)

			reply(msg)

			user.make_damage(10, 15, reply, death=False)

		user.leave(reply)
