from constants import *

name = 'Черное зелье'

description = (
	'Пробирка с каким-то черным зельем.'
)

price = 100
shop_count = 3

usable = True
disposable = True

def on_use(user, reply):
	reply('Это оказалось зелье жизни. Теперь ты здоровее чем мог бы быть.')

	user.heal(user.max_hp // 2)

fightable = True
def fight_use(user, reply, room):
	on_use(user, reply)

	return 0
