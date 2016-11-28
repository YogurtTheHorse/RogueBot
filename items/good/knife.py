from localizations import locale_manager
name = locale_manager.get('items.good.knife.phrase_1')
description = (
	locale_manager.get('items.good.knife.phrase_2')
)

price = 100

fightable = True

def fight_use(user, reply, room):
	return 20