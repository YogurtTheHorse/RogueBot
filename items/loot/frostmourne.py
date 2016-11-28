from localizations import locale_manager
name = locale_manager.get('items.loot.frostmourne.phrase_1')
description = locale_manager.get('items.loot.frostmourne.phrase_2')
price = 3000

fightable = True

def fight_use(user, reply, room):
	return 200