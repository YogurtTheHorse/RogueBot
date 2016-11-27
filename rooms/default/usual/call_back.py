from localizations import locale_manager
name = locale_manager.get('rooms.default.usual.call_back.phrase_1')

def get_actions(user):
	return [ locale_manager.get('rooms.default.usual.call_back.phrase_2')]

def enter(user, reply):
	reply('— Мы вам перезвоним!')

def action(user, reply, text):
	user.leave(reply)