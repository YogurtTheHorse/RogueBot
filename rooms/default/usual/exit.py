from localizations import locale_manager
name = locale_manager.get('rooms.default.usual.exit.phrase_1')

def get_actions(user):
	return [ locale_manager.get('rooms.default.usual.exit.phrase_2'), locale_manager.get('rooms.default.usual.exit.phrase_3')]

def enter(user, reply):
	reply(locale_manager.get('rooms.default.usual.exit.phrase_4'))

def action(user, reply, text):
	if text == locale_manager.get('rooms.default.usual.exit.phrase_5'):
		user.death(reply, reason=locale_manager.get('rooms.default.usual.exit.phrase_6'))
	else:
		user.leave(reply)