from localizations import locale_manager
name = locale_manager.get('rooms.default.usual.watches.phrase_3')

actions_state_0		= [ locale_manager.get('rooms.default.usual.watches.phrase_4'), locale_manager.get('rooms.default.usual.watches.phrase_5') ]  # Начало
actions_state_1		= [ locale_manager.get('rooms.default.usual.watches.phrase_6') ] # Ушел
actions_state_2		= [ locale_manager.get('rooms.default.usual.watches.phrase_7') ] # Остановил
# actions_state_3		= ['']
# actions_state_4		= ['']
# actions_state_5		= ['']
# actions_state_6		= ['']


def get_actions(user):
	if user.has_tag('watches_escape'):
		return actions_state_1
	elif user.has_tag('watches_stop'):
		return actions_state_2
	else:
		return actions_state_0


def enter(user, reply):

	if user.has_tag('watches_escape'):
		reply(locale_manager.get('rooms.default.usual.watches.phrase_8'))

	elif user.has_tag('watches_stop'):
		reply(locale_manager.get('rooms.default.usual.watches.phrase_9'))

	else:
		reply(
			locale_manager.get('rooms.default.usual.watches.phrase_1'))


def action(user, reply, text):

	if user.has_tag('watches_escape'):
		if text == actions_state_1[0]:
			reply(locale_manager.get('rooms.default.usual.watches.phrase_10'))

	elif user.has_tag('watches_stop'):
		if text == actions_state_2[0]:
			reply(locale_manager.get('rooms.default.usual.watches.phrase_11'))

	else:
		if text == actions_state_0[0]:
			reply(
				locale_manager.get('rooms.default.usual.watches.phrase_2'))
			user.add_tag('watches_stop')

		else:
			reply(locale_manager.get('rooms.default.usual.watches.phrase_12'))
			user.add_tag('watches_escape')

	user.leave(reply)

