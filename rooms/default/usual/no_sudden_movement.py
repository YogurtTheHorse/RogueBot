from localizations import locale_manager
from localizations import locale_manager
from time import time
from constants import *

INJURED = 'injured'

name = locale_manager.get('rooms.default.usual.no_sudden_movement.phrase_101')

GO = locale_manager.get('rooms.default.usual.no_sudden_movement.phrase_1')
WAIT = locale_manager.get('rooms.default.usual.no_sudden_movement.phrase_2')

DELTA_TIME_MAX = 15

def get_actions(user):
	return [ GO, WAIT ]

def enter(user, reply):
	reply(locale_manager.get('rooms.default.usual.no_sudden_movement.phrase_102'), photo='BQADAgAD6QgAAmrZzgd8DgIPKNYJ7QI')

	user.set_room_temp('time', time())

def action(user, reply, text):
	t2 = time()
	delta = t2 - user.get_room_temp('time')

	if text == GO:
		if user.has_tag(INJURED) and delta < DELTA_TIME_MAX:
			reply(locale_manager.get('rooms.default.usual.no_sudden_movement.phrase_103'))
			user.death(reply, reason=locale_manager.get('rooms.default.usual.no_sudden_movement.phrase_3'))
		elif delta < DELTA_TIME_MAX:
			reply(locale_manager.get('rooms.default.usual.no_sudden_movement.phrase_104'))
			user.add_tag(INJURED)
			user.make_damage(10, 30, reply, death=False, name=name)
		elif delta > DELTA_TIME_MAX:
			if user.has_tag(INJURED):
				user.remove_tag(INJURED)
			reply(locale_manager.get('rooms.default.usual.no_sudden_movement.phrase_105'))
			user.leave(reply)
	elif text == WAIT:
		if delta < DELTA_TIME_MAX:
			reply(locale_manager.get('rooms.default.usual.no_sudden_movement.phrase_106'))	
		else:
			reply(locale_manager.get('rooms.default.usual.no_sudden_movement.phrase_107'))
