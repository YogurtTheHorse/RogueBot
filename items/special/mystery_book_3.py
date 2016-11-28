from localizations import locale_manager
name = locale_manager.get('items.special.mystery_book_3.phrase_1')

description = locale_manager.get('items.special.mystery_book_3.phrase_2')

price = 1000
	
usable = True

def on_use(user, reply):
	if user.has_item('mystery_book_1') and user.has_item('mystery_book_2'):
		reply(locale_manager.get('items.special.mystery_book_3.phrase_3'))

		user.remove_item('mystery_book_1')
		user.remove_item('mystery_book_2')
		user.remove_item('mystery_book_3')

		user.open_room(reply, 'special', 'bill_cypher')
	else:
		reply(locale_manager.get('items.special.mystery_book_3.phrase_4'))
