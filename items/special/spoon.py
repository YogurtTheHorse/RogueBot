from localizations import locale_manager
name = locale_manager.get('items.special.spoon.phrase_1')
description = (
	locale_manager.get('items.special.spoon.phrase_2')
)

price = 3

fightable = True

def fight_use(user, reply, room):
	return 13