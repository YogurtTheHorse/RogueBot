name = 'М-16'
description = (
	'Приклад немного подплавился и треснул. _Держать вдали от воды!_'
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
