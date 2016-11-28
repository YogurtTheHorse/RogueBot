from localizations import locale_manager
name = locale_manager.get('items.loot.ring.phrase_2')

description = (
	locale_manager.get('items.loot.ring.phrase_1'))

price = 0
iscursed = True


def on_room(user, reply, room):
	reply(locale_manager.get('items.loot.ring.phrase_3'))
	user.make_damage(10, 20, reply, death=False)
