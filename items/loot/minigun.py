name = 'Миниган'
description = (
	'Тратит твои патроны. Быстро.'
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
