from localizations import locale_manager
import random
import usermanager
from constants import *

TOOK_TOOK = locale_manager.get('rooms.default.usual.vladislav.phrase_2')
SPINE = locale_manager.get('rooms.default.usual.vladislav.phrase_3')

name = locale_manager.get('rooms.default.usual.vladislav.phrase_4')

def enter(user, reply):
	msg = (
		locale_manager.get('rooms.default.usual.vladislav.phrase_1'))
	reply(msg)
	user.set_room_temp('question', 'first')

def action(user, reply, text):
	question = user.get_room_temp('question', def_val='first')

	if question == 'first':
		if text == TOOK_TOOK:
			rnd = random.random()
			if rnd < 0.20:
				user.open_room(reply, 'special', 'kiba')
			elif rnd < 0.40:
				user.open_room(reply, 'special', 'kodzima')
			elif rnd < 0.60:
				user.open_room(reply, 'special', 'gabe')
			elif rnd < 0.80:
				user.open_room(reply, 'special', 'yegorf1')
			else:
				user.open_room(reply, 'special', 'bill_gates')
		elif text == SPINE:
			reply(locale_manager.get('rooms.default.usual.vladislav.phrase_5'))
			user.set_room_temp('question', 'spine')
	elif question == 'spine':
		reply(locale_manager.get('rooms.default.usual.vladislav.phrase_6'))
		user.make_damage(10, 15, reply, False)

		user.leave(reply)

def get_actions(user):
	question = user.get_room_temp('question', def_val='first')
	ans = [ ]

	if question == 'first':
		ans = [ TOOK_TOOK, SPINE ]
	else:
		ans = [ locale_manager.get('rooms.default.usual.vladislav.phrase_7') ]

	return ans