from localizations import locale_manager
name = locale_manager.get('items.loot.m-16.phrase_1')
description = (
	locale_manager.get('items.loot.m-16.phrase_2')
)

price = 300

fightable = True

strengthoff = True

def fight_use(user, reply, room):
	res = 0
	while user.has_item('bullet') and res // 30 < 20:
		user.remove_item('bullet')
		res += 30
	return res
