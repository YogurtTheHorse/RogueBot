from localizations import locale_manager
name = locale_manager.get('rooms.default.usual.uncle_stanley.phrase_1')

def get_actions(user):
	return [locale_manager.get('rooms.default.usual.uncle_stanley.phrase_2')]

def enter(user, reply):
	reply(locale_manager.get('rooms.default.usual.uncle_stanley.phrase_3'))


def action(user, reply, text):
	if user.has_item('mystery_book_1'):
		reply(locale_manager.get('rooms.default.usual.uncle_stanley.phrase_4'))
	else:
		user.add_item('special', 'mystery_book_1')

	user.leave(reply)
