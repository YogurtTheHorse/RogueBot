from localizations import locale_manager
from localizations import locale_manager
name = locale_manager.get('rooms.default.usual.door.phrase_1')

actions = [ locale_manager.get('rooms.default.usual.door.phrase_2'), locale_manager.get('rooms.default.usual.door.phrase_3')]

def get_actions(user):
	return actions

def enter(user, reply):
	reply(locale_manager.get('rooms.default.usual.door.phrase_4'), photo='BQADAgAD9wgAAmrZzgfQsNScN9T3LwI')
	user.set_room_temp('cnt', 0)

def action(user, reply, text):
	if text == actions[0]:
		cnt = user.get_room_temp('cnt', def_val=0)
		if cnt > 10:
			reply(locale_manager.get('rooms.default.usual.door.phrase_101'))
		elif cnt > 20:
			reply(locale_manager.get('rooms.default.usual.door.phrase_102'))
			user.death(reply, reason=locale_manager.get('rooms.default.usual.door.phrase_5'))
		reply(locale_manager.get('rooms.default.usual.door.phrase_103'))
		user.set_room_temp('cnt', cnt+1)
	else:
		reply(locale_manager.get('rooms.default.usual.door.phrase_6'))
		user.leave(reply)