from localizations import locale_manager
import random

name = random.choice([locale_manager.get('rooms.default.usual.nothing.phrase_1'), locale_manager.get('rooms.default.usual.nothing.phrase_2'), locale_manager.get('rooms.default.usual.nothing.phrase_3'), locale_manager.get('rooms.default.usual.nothing.phrase_4'), locale_manager.get('rooms.default.usual.nothing.phrase_5')])
not_for_sign = True

def get_actions(user):
	return [ locale_manager.get('rooms.default.usual.nothing.phrase_6')]

def enter(user, reply):
	reply(locale_manager.get('rooms.default.usual.nothing.phrase_7'))

def action(user, reply, text):
	user.open_room(reply)
