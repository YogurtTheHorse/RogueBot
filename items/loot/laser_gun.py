name = 'Лазерный пистолет'
description = (
	'Хороший такой ЛАЗЕРНЫЙ пистолет'
)

price = 300

fightable = True

def fight_use(user, reply, room):
	if user.has_item('laser_bullet'):
		reply('БАХ! Выстрел!')

		user.remove_item('laser_bullet')

		return 60
	else:
		reply('Пластикавая пулялка не работает без патронов. А жаль')

		return 0