from localizations import locale_manager
name = locale_manager.get('items.loot.minigun.phrase_1')
description = (
	locale_manager.get('items.loot.minigun.phrase_2')
)

price = 650

fightable = True

strengthoff = True

def fight_use(user, reply, room):
	res = 10
	while user.has_item('bullet') and res // 5 < 40:
		user.remove_item('bullet')
		res += 5
	return res
