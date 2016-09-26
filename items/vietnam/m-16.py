name = 'М-16'
description = (
    'Почти не заржавела'
)

price = 300

fightable = True

strengthoff = True

def fight_use(user, reply, room):
	res = 0
	while user.has_item('bullet') and res // 60 < 10:
		user.remove_item('bullet')
		res += 60
	return res
