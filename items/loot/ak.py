name = 'АК-47'
description = (
	' Пробивает рельс. Насвозь. Вдоль. Наверное.'
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
