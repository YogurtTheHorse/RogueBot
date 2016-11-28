from localizations import locale_manager
name = locale_manager.get('items.special.trident.phrase_1')
description = (
	locale_manager.get('items.special.trident.phrase_2')
)

price = 500

fightable = True

def fight_use(user, reply, room):
	return 30