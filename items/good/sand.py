from localizations import locale_manager
name = locale_manager.get('items.good.sand.phrase_1')
description = (
	locale_manager.get('items.good.sand.phrase_2')
)

price = 99

fightable = True

strengthoff = True

disposable = True
def fight_use(user, reply, room):
	return 99