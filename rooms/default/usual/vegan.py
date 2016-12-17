from localizations import locale_manager
name = locale_manager.get('rooms.default.usual.vegan.phrase_1')

actions = [ locale_manager.get('rooms.default.usual.vegan.phrase_2'), locale_manager.get('rooms.default.usual.vegan.phrase_3')]

def get_actions(user):
	return actions

def enter(user, reply):
	reply(locale_manager.get('rooms.default.usual.vegan.main'))

def action(user, reply, text):
	if text == actions[0]:
		reply(locale_manager.get('rooms.default.usual.vegan.main'))
	else:
		reply(locale_manager.get('rooms.default.usual.vegan.phrase_4'))
		user.leave(reply)