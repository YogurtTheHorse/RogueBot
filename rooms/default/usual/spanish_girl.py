from localizations import locale_manager
from constants import *

READY = locale_manager.get('rooms.default.usual.spanish_girl.phrase_5')
ESCAPE = locale_manager.get('rooms.default.usual.spanish_girl.phrase_6')
CLOSER = locale_manager.get('rooms.default.usual.spanish_girl.phrase_7')

name = locale_manager.get('rooms.default.usual.spanish_girl.phrase_8')

def enter(user, reply):
	msg = ( 
		locale_manager.get('rooms.default.usual.spanish_girl.phrase_1'))
	reply(msg)
	user.set_room_temp('question', 'first')

def action(user, reply, text):
	question = user.get_room_temp('question', def_val='first')

	if question == 'first':
		if text  == READY:
			reply(locale_manager.get('rooms.default.usual.spanish_girl.phrase_9'))
			user.set_room_temp('question', 'undress')
		else:
			reply(locale_manager.get('rooms.default.usual.spanish_girl.phrase_10'))
			user.leave(reply)
	elif question == 'undress':
		if text == CLOSER:
			if user.has_item('christ'):
				reply(
					locale_manager.get('rooms.default.usual.spanish_girl.phrase_2') + locale_manager.get('rooms.default.usual.spanish_girl.phrase_3'), photo='BQADAgAD8wgAAmrZzgci29uXEW-PPgI'
				)
				user.add_item('special', 'wine')
				user.leave(reply)
			else:
				msg = locale_manager.get('rooms.default.usual.spanish_girl.phrase_4') + '..\n' + locale_manager.get('rooms.default.usual.spanish_girl.phrase_11')
				reply(msg, photo='BQADAgAD8wgAAmrZzgci29uXEW-PPgI')
				user.throw_dice(reply, 'burn')
		else:
			reply(locale_manager.get('rooms.default.usual.spanish_girl.phrase_12'))
			user.leave(reply)

def get_actions(user):
	question = user.get_room_temp('question', def_val='first')
	ans = [ ]

	if question == 'first':
		ans = [ READY, ESCAPE ]
	else:
		ans = [ CLOSER, ESCAPE]

	return ans

def dice(user, reply, result, subject='burn'):
	if result > DICE_MIDDLE:
		reply(locale_manager.get('rooms.default.usual.spanish_girl.phrase_13'))
		user.leave(reply)
	else:
		reply(locale_manager.get('rooms.default.usual.spanish_girl.phrase_14'))
		user.death(reply, reason=locale_manager.get('rooms.default.usual.spanish_girl.phrase_15'))	
