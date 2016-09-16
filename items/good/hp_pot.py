from constants import *

name = 'Черное зелье'

description = (
	'Пробирка с каким-то черным зельем.'
)

price = 100
shop_count = 2

usable = True
disposable = True

def on_use(user, reply):
	reply('Это оказалось зелье жизни. Теперь ты здоровее чем мог бы быть.')

	user.hp = user.max_hp

fightable = True
def fight_use(user, reply, room):
	on_use(user, reply)

	return 0
