from time import time
from constants import *

name = '_Вода_'

CHEST = 'Ты видишь сундук! Доплыть до него'
FAST = 'Как можно быстрее закрыть дверь пока ты весь не промок'

DELTA_TIME_MAX = 5

def get_actions(user):
	return [ CHEST, FAST ]

def dice(user, reply, result, subject=None):
	if result > DICE_MIDDLE:
		reply('Ты все таки доплыл! Там лежал трезубец.')
		
		user.add_tag('wet')
		user.add_item('special', 'trident')
	else:
		reply('Что-то пошло не так и тебя все равно смыло в коридор.')
		user.make_damage(0, 10, reply, False)
		user.add_tag('wet')

	user.leave(reply)

def enter(user, reply):
	msg = (
		'_Чувак_, тут полная комната _воды!_\n'
		'По непонятным причинам вода стоит стеной, но это ненадолго.\n'
		'Думай *быстрее*.'
	)

	user.set_room_temp('time', time())

	reply(msg)

def action(user, reply, text):
	t2 = time()
	delta = t2 - user.get_room_temp('time')

	if delta > DELTA_TIME_MAX:
		msg = (
			'За {0:.2f} секунд можно было определиться!\n'
			'Тебя смыло большой волной в коридор и ударило об стены.'
		).format(delta)

		user.add_tag('wet')
		user.make_damage(10, 20, reply, False)
		user.leave(reply)

		reply(msg)
	elif text == CHEST:
		user.throw_dice(reply, text)
	elif text == FAST:
		reply('Еле успел. Ух.')

		user.leave(reply)
	else:
		reply('Думай быстрее!')
