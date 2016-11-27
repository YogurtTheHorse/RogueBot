from localizations import locale_manager
from constants import *
import bossmanager
import random

name = locale_manager.get('rooms.default.usual.fog_door.phrase_5')

actions_enter =  [ locale_manager.get('rooms.default.usual.fog_door.phrase_6'), locale_manager.get('rooms.default.usual.fog_door.phrase_7') ]
actions_try_to_see = [ locale_manager.get('rooms.default.usual.fog_door.phrase_8'), locale_manager.get('rooms.default.usual.fog_door.phrase_9') ]
actions_pass_throw_fog = [ locale_manager.get('rooms.default.usual.fog_door.phrase_10'), locale_manager.get('rooms.default.usual.fog_door.phrase_11') ]

def can_open(user, reply):
	return not user.has_tag(DEVIL)

def open_failure(user, reply):
	reply(locale_manager.get('rooms.default.usual.fog_door.phrase_12'))

def enter(user, reply):
	msg = (
		locale_manager.get('rooms.default.usual.fog_door.phrase_1'))

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
			locale_manager.get('rooms.default.usual.fog_door.phrase_2'))

		reply(msg)

		user.set_room_temp('question', 'try_to_see')

	else:
		msg = (
			locale_manager.get('rooms.default.usual.fog_door.phrase_13')
		)

		reply(msg)

		user.leave(reply)


def action_try_to_see(user, reply, text):
	if text == actions_try_to_see[0]:
		boss = bossmanager.current()

		if boss['alive']:
			msg = (
				locale_manager.get('rooms.default.usual.fog_door.phrase_3'))

			reply(msg)

			user.set_room_temp('question', 'pass_throw_fog')

		else:
			msg = (
				locale_manager.get('rooms.default.usual.fog_door.phrase_4'))

			reply(msg)

			user.leave(reply)

	else:
		msg = (
			locale_manager.get('rooms.default.usual.fog_door.phrase_14')
		)

		reply(msg)

		user.leave(reply)


def action_pass_throw_fog(user, reply, text):
	if text == actions_pass_throw_fog[0]:
		msg = locale_manager.get('rooms.default.usual.fog_door.phrase_15') + '...\n' +  '...\n' + '...'

		reply(msg)

		boss = bossmanager.current()

		user.open_room(reply, 'boss', boss['name'])

	else:
		random_number = random.random()

		if random_number < 0.2:
			msg = (
				locale_manager.get('rooms.default.usual.fog_door.phrase_16')
			)

			reply(msg)

		else:
			msg = (
				locale_manager.get('rooms.default.usual.fog_door.phrase_17')
			)

			reply(msg)

			user.make_damage(10, 15, reply, death=False)

		user.leave(reply)
