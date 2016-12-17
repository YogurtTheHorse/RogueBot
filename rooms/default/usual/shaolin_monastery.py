from localizations import locale_manager
from localizations import locale_manager
from constants import *

name = locale_manager.get('rooms.default.usual.shaolin_monastery.phrase_1')

room_type = 'other'

def get_actions(user):
	return [ locale_manager.get('rooms.default.usual.shaolin_monastery.phrase_2'), locale_manager.get('rooms.default.usual.shaolin_monastery.phrase_3'), locale_manager.get('rooms.default.usual.shaolin_monastery.phrase_4')]

def enter(user, reply):
	reply(locale_manager.get('rooms.default.usual.shaolin_monastery.phrase_5'), photo='BQADAgADFQkAAmrZzgeH6hmh7PbRYgI')

def action(user, reply, text):
	actions = get_actions(user)

	if text == actions[0]:
		user.throw_dice(reply, 'fragile')
	elif text == actions[1]:
		user.defence += 5
		reply(locale_manager.get('rooms.default.usual.shaolin_monastery.phrase_101'), photo='BQADAgADFAkAAmrZzgfPUvv4wiphMQI')
		if not user.paid(50):
			reply(locale_manager.get('rooms.default.usual.shaolin_monastery.phrase_6'))
			user.make_damage(20, 60, reply, name=name)
		user.leave(reply)
	else:
		if user.has_item('tin_foil_hat'):
			reply(locale_manager.get('rooms.default.usual.shaolin_monastery.phrase_102'))
		user.throw_dice(reply, 'escape')

def dice(user, reply, result, subject=None):
	if subject == 'fragile':
		if result > DICE_MIDDLE:
			reply(locale_manager.get('rooms.default.usual.shaolin_monastery.phrase_103'))
			user.leave(reply)
		else:
			reply(locale_manager.get('rooms.default.usual.shaolin_monastery.phrase_104'))
			user.make_damage(50, 80, reply, name=name)
			user.leave(reply)
	elif subject == 'escape':
		if result > (DICE_MAX / 4) * 3:
			reply(locale_manager.get('rooms.default.usual.shaolin_monastery.phrase_105'))
			user.leave(reply)
		else:
			reply(locale_manager.get('rooms.default.usual.shaolin_monastery.phrase_106'))
			user.make_damage(50, 80, reply, name=name)
			user.leave(reply)	
