from localizations import locale_manager
name = locale_manager.get('items.special.intoxicated_shoes.phrase_1')
description = locale_manager.get('items.special.intoxicated_shoes.phrase_2')

price = 0
iscursed = True

def on_room(user, reply, room):
	reply(locale_manager.get('items.special.intoxicated_shoes.phrase_3'))
	user.make_damage(5, 10, reply, death=False)