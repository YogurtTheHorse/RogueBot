from localizations import locale_manager
import random
import usermanager
from constants import *

HOW = locale_manager.get('rooms.default.special.kodzima.phrase_5')
JOKE = locale_manager.get('rooms.default.special.kodzima.phrase_6')
ASK = locale_manager.get('rooms.default.special.kodzima.phrase_7')

ANYTHING_ELSE = locale_manager.get('rooms.default.special.kodzima.phrase_8')
SLIME = locale_manager.get('rooms.default.special.kodzima.phrase_9')

BRAINSTORM = locale_manager.get('rooms.default.special.kodzima.phrase_10')
TAKE_SPOON = locale_manager.get('rooms.default.special.kodzima.phrase_11')

name = locale_manager.get('rooms.default.special.kodzima.phrase_12')

def enter(user, reply):
	msg = (
		locale_manager.get('rooms.default.special.kodzima.phrase_1')
	)
	reply(msg.format(user.name))
	user.set_room_temp('question', 'first')

def action(user, reply, text):
	question = user.get_room_temp('question', def_val='first')

	if question == 'first':
		if text == HOW:
			user1 = usermanager.random_user()
			user2 = usermanager.random_user()
			name1 = user1.name
			name2 = user2.name

			reply(locale_manager.get('rooms.default.special.kodzima.phrase_13').format(name1, name2))

			reply(locale_manager.get('rooms.default.special.kodzima.phrase_14'))
			user.leave(reply)
		elif text == ASK:
			reply(locale_manager.get('rooms.default.special.kodzima.phrase_15'))
			user.set_room_temp('question', 'question')
		else:
			reply(locale_manager.get('rooms.default.special.kodzima.phrase_16'))
			user.make_damage(25, 50, reply, False)

			reply(locale_manager.get('rooms.default.special.kodzima.phrase_17'))
			user.leave(reply)
	elif question == 'question':
		if text == ANYTHING_ELSE:
			msg = (
				locale_manager.get('rooms.default.special.kodzima.phrase_2'))
			reply(msg)
			user.set_room_temp('question', 'spoon')
		else:
			msg = (
				locale_manager.get('rooms.default.special.kodzima.phrase_3'))
			reply(msg.format(user.name))
			user.set_room_temp('question', 'slime')
	elif question == 'slime':
		reply(locale_manager.get('rooms.default.special.kodzima.phrase_18') + locale_manager.get('rooms.default.special.kodzima.phrase_4'))
		user.add_item('special', 'spoilers')
		user.leave(reply)
	elif question == 'spoon':
		if text == BRAINSTORM:
			reply(locale_manager.get('rooms.default.special.kodzima.phrase_19'))
			user.death(reply, reason=locale_manager.get('rooms.default.special.kodzima.phrase_20'))
		else:
			reply(locale_manager.get('rooms.default.special.kodzima.phrase_21'))
			user.add_item('special', 'good_spoon')
			user.leave(reply)



def get_actions(user):
	question = user.get_room_temp('question', def_val='first')
	ans = [ ]

	if question == 'first':
		if user.get_mana_damage() < 7:
			ans = [ HOW, JOKE ]
		else:
			ans = [ ASK ]
	elif question == 'question':
		ans = [ ANYTHING_ELSE, SLIME ]
	elif question == 'spoon':
		return [ BRAINSTORM, TAKE_SPOON ]
	elif question == 'slime':
		ans = [ locale_manager.get('rooms.default.special.kodzima.phrase_22') ]
	else:
		ans = [ locale_manager.get('rooms.default.special.kodzima.phrase_23') ]

	return ans
