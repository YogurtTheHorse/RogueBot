from localizations import locale_manager
name = locale_manager.get('items.loot.knight_sword.phrase_1')
description = locale_manager.get('items.loot.knight_sword.phrase_2')
price = 150

fightable = True

def fight_use(user, reply, room):
	return 70