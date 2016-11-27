from localizations import locale_manager
name = locale_manager.get('rooms.vietnam.missions_main.third.phrase_1')

actions = [ locale_manager.get('rooms.vietnam.missions_main.third.phrase_2'), locale_manager.get('rooms.vietnam.missions_main.third.phrase_3')]

def get_actions(user):
	return actions

def enter(user, reply):
	reply(locale_manager.get('rooms.vietnam.missions_main.third.phrase_4'))
	reply(locale_manager.get('rooms.vietnam.missions_main.third.phrase_5'))

def action(user, reply, text):
	if text == actions[0]:
		reply(locale_manager.get('rooms.vietnam.missions_main.third.phrase_6'))
	
	user.leave(reply)