from localizations import locale_manager
name = locale_manager.get('items.loot.ak.phrase_1')
description = (
	locale_manager.get('items.loot.ak.phrase_2')
)

price = 300

fightable = True

strengthoff = True

def fight_use(user, reply, room):
	res = 0
	while user.has_item('bullet') and res // 60 < 30:
		user.remove_item('bullet')
		res += 60
	return res
