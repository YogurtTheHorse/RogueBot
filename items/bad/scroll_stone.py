from constants import *

name = 'Свиток вызова камней'

description = (
	'Все что о нем известно, так это то что на нем нарисован камень.'
)

price = 200

fightable = True
disposable = True

def fight_use(user, reply, room):
	if user.use_mana(50):
		reply('С неба падают камни прямо на тебя и наносят 50 урона.')
		user.make_damage(50, 100, reply, death=True, name='Камнепад')
	else:
		reply('Недостаточно маны')
		user.add_item('bad', 'scroll_stone')
	return 0
