from localizations import locale_manager
name = locale_manager.get('rooms.default.missions_main.second.phrase_1')

actions = [ locale_manager.get('rooms.default.missions_main.second.phrase_2'), locale_manager.get('rooms.default.missions_main.second.phrase_3')]

def get_actions(user):
	return actions

def enter(user, reply):
	reply(locale_manager.get('rooms.default.missions_main.second.phrase_7'))
	reply(locale_manager.get('rooms.default.missions_main.second.phrase_8'))

	if user.get_charisma() > 10:
		reply(locale_manager.get('rooms.default.missions_main.second.phrase_4'))
		user.new_mission('main', 'third', 15)
	else:
		reply(locale_manager.get('rooms.default.missions_main.second.phrase_5'))
		user.new_mission('main', 'second', 15)

def action(user, reply, text):
	if text == actions[0]:
		reply(locale_manager.get('rooms.default.missions_main.second.phrase_6'))
	else:
		user.leave(reply)