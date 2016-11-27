from localizations import locale_manager
import databasemanager
import tornamentmanager

name = locale_manager.get('rooms.default.usual.cesar.phrase_1')

actions = [ locale_manager.get('rooms.default.usual.cesar.phrase_2'), locale_manager.get('rooms.default.usual.cesar.phrase_3')]

def get_actions(user):
	return actions

def enter(user, reply):
	reply(locale_manager.get('rooms.default.usual.cesar.phrase_4'))
	reply(
		locale_manager.get('rooms.default.usual.cesar.phrase_5'),
		photo='BQADAgADTgkAAmrZzgdMf1IntNiY4wI'
	)

def action(user, reply, text):
	if text == actions[0]:
		if user.get_damage() > 100:
			reply(locale_manager.get('rooms.default.usual.cesar.phrase_6'))
		elif databasemanager.get_variable('ces', def_val=False) is False:
			reply(locale_manager.get('rooms.default.usual.cesar.phrase_7'))
		else:
			reply(locale_manager.get('rooms.default.usual.cesar.phrase_8'))
			if tornamentmanager.add_to_list('cesar', user.uid) < 0:
				reply(locale_manager.get('rooms.default.usual.cesar.phrase_9'))
	else:
		reply(locale_manager.get('rooms.default.usual.cesar.phrase_10'))
	user.leave(reply)
