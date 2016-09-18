name = 'Лазерный пистолет'
description = (
	'Хороший такой ЛАЗЕРНЫЙ пистолет.'
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
