name = 'Пистолет'
description = (
	'Хороший такой пистолет. 20 миллиметров.'
)

price = 300

fightable = True

strengthoff = True

def fight_use(user, reply, room):
	if user.has_item('bullet'):
		reply('БАХ! Выстрел!')

		user.remove_item('bullet')

		return 30
	else:
		reply('Патроны закончились, но ты не дрейфь. Весит эта штука достаточно.')

		return 10