from localizations import locale_manager
name = 'M79'
description = (
	locale_manager.get('items.loot.m79.phrase_1')
)

price = 800

fightable = True

strengthoff = True

def fight_use(user, reply, room):
	res = 400
	while user.has_item('bullet') and res // 20 < 10:
		user.remove_item('bullet')
		res += 20
	return res
