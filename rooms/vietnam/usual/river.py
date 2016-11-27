from localizations import locale_manager
name = locale_manager.get('rooms.vietnam.usual.river.phrase_3')


def get_actions(user):
	return [ locale_manager.get('rooms.vietnam.usual.river.phrase_4'), locale_manager.get('rooms.vietnam.usual.river.phrase_5') ]


def enter(user, reply):
	reply(
		locale_manager.get('rooms.vietnam.usual.river.phrase_1'))
	user.set_room_temp('rvr', 0)

def action(user, reply, text):
	if text == locale_manager.get('rooms.vietnam.usual.river.phrase_6'):
		user.leave(reply)
		return

	rvr = user.get_room_temp('rvr', 0)

	if user.has_item('m79') :
		rvr += 4
		reply(locale_manager.get('rooms.vietnam.usual.river.phrase_7'))
	else:
		rvr += 1
		reply(locale_manager.get('rooms.vietnam.usual.river.phrase_8'))
	
	user.set_room_temp('rvr', rvr)

	if rvr > 8:
		msg = ''
		if user.has_item('m-16'):
			user.remove_item('m-16')
			reply(locale_manager.get('rooms.vietnam.usual.river.phrase_9'))


		reply(
			locale_manager.get('rooms.vietnam.usual.river.phrase_2'))

		user.rooms_pack = 'default'
		user.leave(reply)
