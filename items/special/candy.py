import random

from utils.buffs import DiabetBuff

name = 'Конфетка'
description = (
	'Сладкая и вкусная'
)

price = 1

usable = True
disposable = True

def on_use(user, reply):
	cnt = user.get_variable('candies_eat', 0)

	if cnt == 10:
		reply('Поздравляю, у вас диабет!')
		reply('Вот вам конфетка без сахара, чтобы утешить себя')

		user.new_buff(DiabetBuff())
		user.add_item('special', 'candy')
	elif cnt == 11:
		reply('А нет, это с сахаром :(\nВот вам другая.')
		user.add_item('special', 'candy')
		user.make_damage(3, 7, reply, name='Диабет')
	elif cnt > 11:
		reply('Ну что же вы себя убиваете, голубчик!')
		user.make_damage(cnt - 5, cnt + 3, reply, name='Диабет')
	else:
		reply('Вкусненько!')
		user.heal(15)

	user.get_variable('candies_eat', cnt + 1)