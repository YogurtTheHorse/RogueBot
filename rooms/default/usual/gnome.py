from localizations import locale_manager
from constants import *
import databasemanager

name = locale_manager.get('rooms.default.usual.gnome.phrase_1')

def get_actions(user):
	actions = [ '10' ] + [ str((g + 1) * 50) for g in range(min(user.gold // 50, 9)) ]

	return actions

def can_open(user, reply):
	return not user.has_tag(DEVIL)

def open_failure(user, reply):
	reply(locale_manager.get('rooms.default.usual.gnome.phrase_2'))

def enter(user, reply):
	reply(locale_manager.get('rooms.default.usual.gnome.phrase_3'))

def action(user, reply, text):
	try:
		integer = int(text)

		if user.paid(integer) and integer > 0:
			reply('«Держи эту прекрасную ложку ручной работы!»')

			user.add_item('special', 'spoon')
			databasemanager.add_to_leaderboard(user, integer, databasemanager.GNOME_TABLE)
		else:
			reply(locale_manager.get('rooms.default.usual.gnome.phrase_4'))
			user.gold = 0

		user.leave(reply)
	except:
		reply(locale_manager.get('rooms.default.usual.gnome.phrase_5'))
