from localizations import locale_manager
name = locale_manager.get('rooms.default.usual.lepricone.phrase_1')

def on_enter(user, reply):
	reply(
		locale_manager.get('rooms.default.usual.lepricone.phrase_2'))

def get_actions(user):
	return [ locale_manager.get('rooms.default.usual.lepricone.phrase_3'), locale_manager.get('rooms.default.usual.lepricone.phrase_4')]

def action(user, reply, text):
	if text == locale_manager.get('rooms.default.usual.lepricone.phrase_5'):
		user.gold += 250
		user.new_mission('lepricone', path_len=7)
		reply(locale_manager.get('rooms.default.usual.lepricone.phrase_6'))

	user.leave(reply)
