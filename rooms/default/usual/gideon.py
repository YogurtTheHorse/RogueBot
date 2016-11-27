from localizations import locale_manager
from constants import *

FIGHT = locale_manager.get('rooms.default.usual.gideon.phrase_1')

name = locale_manager.get('rooms.default.usual.gideon.phrase_2')

def enter(user,reply):
	reply(locale_manager.get('rooms.default.usual.gideon.phrase_3'))
	user.throw_dice(reply)

def dice(user, reply, result, subject=None):
	if result > DICE_MAX:
		reply(locale_manager.get('rooms.default.usual.gideon.phrase_4'))
		if not user.has_item('mystery_book_2'):
			reply(locale_manager.get('rooms.default.usual.gideon.phrase_5'))
			user.add_item('special', 'mystery_book_2')
		user.leave(reply)
	else:
		reply(locale_manager.get('rooms.default.usual.gideon.phrase_6'))
		user.leave(reply)

def get_actions(user):
	return []

def action(user, reply, text):
	pass