from localizations import locale_manager
name = locale_manager.get('items.loot.laser_gun.phrase_1')
description = (
	locale_manager.get('items.loot.laser_gun.phrase_2')
)

price = 300

fightable = True

strengthoff = True

def fight_use(user, reply, room):
	res = 0
	while user.has_item('laser_bullet') and res // 60 < 10:
		user.remove_item('laser_bullet')

		res += 60
	return res
