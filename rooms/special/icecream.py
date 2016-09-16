from constants import *

name = 'Озеро из мороженного'

room_type = 'other'
actions = [ 'Набрать себе', 'Съесть как можно больше', 'Выйти' ]

def get_actions(user):
	return actions

def dice(user, reply, result, subject=None):
	if result > DICE_MIDDLE:
		reply('Неплохо, но у Толи слишком мало клиентов, чтобы еще и платить несостоявшимся искателям приключений, поэтому пойдем поищем чего еще')
	else:
		reply('Мда. Тебя избили битой за то, что ты сломал ножницы.')

		if user.has_item('scissors'):
			user.remove_items_with_tag('scissors')
			reply('О. Так у тебя есть ножницы. Ну и их отберем!')

		user.make_damage(20, 30, reply, death=False)
	user.leave(reply)

def enter(user, reply):
	msg = 'Настоящие озеро мороженного.\nРазвлекайся.'
	reply(msg)

def action(user, reply, text):
	if text == actions[0]:
		reply('Держи рожок мороженого')

		user.add_item('special', 'icecream')
	elif text == actions[1]:
		if user.gods_level[BUDDHA_NUM] > 0:
			reply('Ты не следовал восмеричному пути и слегка испортил баланс кармы в своей жизни.')
			user.gods_level[BUDDHA_NUM] = 0
		else:
			reply('Вкусно и _больно_')
			user.make_damage(1, 5, reply, death=False)
	else:
		user.leave(reply)
