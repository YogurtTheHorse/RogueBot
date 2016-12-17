from localizations import locale_manager
from time import time
from constants import *

name = locale_manager.get('rooms.default.usual.water.name')

CHEST = locale_manager.get('rooms.default.usual.water.phrase_2')
FAST = locale_manager.get('rooms.default.usual.water.phrase_3')

DELTA_TIME_MAX = 5

def get_actions(user):
	return [ CHEST, FAST ]

def dice(user, reply, result, subject=None):
	if result > DICE_MIDDLE:
		reply(locale_manager.get('rooms.default.usual.water.phrase_4'))
		
		user.add_tag('wet')
		user.add_item('special', 'trident')
	else:
		reply(locale_manager.get('rooms.default.usual.water.phrase_5'))
		user.make_damage(0, 10, reply, False)
		user.add_tag('wet')

	user.leave(reply)

def enter(user, reply):
	msg = locale_manager.get('rooms.default.usual.water.phrase_1')

	user.set_room_temp('time', time())

	reply(msg)

def action(user, reply, text):
	t2 = time()
	delta = t2 - user.get_room_temp('time')

	if delta > DELTA_TIME_MAX:
		msg = locale_manager.get('rooms.default.usual.water.phrase_6').format(delta)

		user.add_tag('wet')
		user.make_damage(10, 20, reply, False)
		user.leave(reply)

		reply(msg)
	elif text == CHEST:
		user.throw_dice(reply, text)
	elif text == FAST:
		reply(locale_manager.get('rooms.default.usual.water.phrase_7'))

		user.leave(reply)
	else:
		reply(locale_manager.get('rooms.default.usual.water.phrase_8'))
