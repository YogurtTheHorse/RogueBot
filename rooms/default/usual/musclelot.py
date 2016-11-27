from localizations import locale_manager
from constants import *

LASER_ESCAPE = 'tried_escape'

name = locale_manager.get('rooms.default.usual.musclelot.phrase_5')

room_type = 'other'

def get_actions(user):
	if user.has_tag(EVIL_MUSCLELOT):
		actions = [ locale_manager.get('rooms.default.usual.musclelot.phrase_6') ]
		if user.has_item('laser'):
			actions.append(locale_manager.get('rooms.default.usual.musclelot.phrase_7'))

		return actions
	else:
		if user.get_room_temp(LASER_ESCAPE, False):
			return [ locale_manager.get('rooms.default.usual.musclelot.phrase_8'), locale_manager.get('rooms.default.usual.musclelot.phrase_9'), locale_manager.get('rooms.default.usual.musclelot.phrase_10'), locale_manager.get('rooms.default.usual.musclelot.phrase_11') ]
		else:
			return [ locale_manager.get('rooms.default.usual.musclelot.phrase_12'), locale_manager.get('rooms.default.usual.musclelot.phrase_13'), locale_manager.get('rooms.default.usual.musclelot.phrase_14'), locale_manager.get('rooms.default.usual.musclelot.phrase_15') ]

def enter(user, reply):
	if user.has_tag(EVIL_MUSCLELOT):
		msg = (
			locale_manager.get('rooms.default.usual.musclelot.phrase_1'))
		reply(msg)
	else:
		msg = (
			locale_manager.get('rooms.default.usual.musclelot.phrase_2'))
		reply(msg, photo='BQADAgAD1AgAAmrZzgcux0BHbF1X1gI')

def action(user, reply, text):
	if user.has_tag(EVIL_MUSCLELOT):
		evil_action(user, reply, text)
	else:
		normal_action(user, reply, text)

def evil_action(user, reply, text):
	actions = get_actions(user)

	if text == actions[0]:
		user.throw_dice(reply, 'fight')
	elif len(actions) > 1 and text == actions[1]:
		msg = (
			locale_manager.get('rooms.default.usual.musclelot.phrase_3'))
		reply(msg)

		user.make_damage(30, 40, reply, name=name)
		user.steal(20)
		user.leave(reply)

def normal_action(user, reply, text):
	actions = get_actions(user)

	if text == actions[0]:
		user.throw_dice(reply, 'zhmesh')
	elif text == actions[1]:
		usr_name = user.name.lower()
		if (locale_manager.get('rooms.default.usual.musclelot.phrase_16') in usr_name) or (locale_manager.get('rooms.default.usual.musclelot.phrase_17') in usr_name) or (locale_manager.get('rooms.default.usual.musclelot.phrase_18') in usr_name):
			reply(locale_manager.get('rooms.default.usual.musclelot.phrase_19'))
			user.throw_dice(reply, 'five')
		else:
			reply(locale_manager.get('rooms.default.usual.musclelot.phrase_20').format(usr_name))
	elif text == actions[2]:
		user.damage += 5
		reply(locale_manager.get('rooms.default.usual.musclelot.phrase_21'))
		if not user.paid(50):
			msg = (
				locale_manager.get('rooms.default.usual.musclelot.phrase_4'))
			reply(msg)
			user.make_damage(40, 60, reply, name=name)
		user.leave(reply)
	elif text == actions[3]:
		if user.get_room_temp(LASER_ESCAPE, False):
			reply(locale_manager.get('rooms.default.usual.musclelot.phrase_22'))
			user.escape(reply, True)
			user.add_tag(EVIL_MUSCLELOT)
		else:
			reply(locale_manager.get('rooms.default.usual.musclelot.phrase_23'))
			user.escape(reply, False)

			if user.has_item('laser'):
				user.set_room_temp(LASER_ESCAPE, True)

def dice(user, reply, result, subject='zhmesh'):
	if result > DICE_MIDDLE:
		if subject == 'zhmesh':
			reply(locale_manager.get('rooms.default.usual.musclelot.phrase_24'))
		elif subject == 'fight':
			reply(locale_manager.get('rooms.default.usual.musclelot.phrase_25'))
			user.make_damage(5, 10, reply, False, name=name)
		else:
			reply(locale_manager.get('rooms.default.usual.musclelot.phrase_26'))

		reply(locale_manager.get('rooms.default.usual.musclelot.phrase_27'))
	else:
		if subject == 'zhmesh':
			reply(locale_manager.get('rooms.default.usual.musclelot.phrase_28'))
			user.make_damage(5, 10, reply, name=name)
		elif subject == 'fight':
			reply(locale_manager.get('rooms.default.usual.musclelot.phrase_29'))
			user.make_damage(50, 60, reply, name=name)
		else:
			reply(locale_manager.get('rooms.default.usual.musclelot.phrase_30'))
			user.make_damage(5, 10, reply, name=name)
	user.leave(reply)
