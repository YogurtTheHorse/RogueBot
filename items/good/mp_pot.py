from constants import *

name = 'Красное зелье'

description = (
	'Пробирка с каким-то красным зельем.'
)

price = 100
shop_count = 3

usable = True
disposable = True

def on_use(user, reply):
	reply('Это оказалось зелье маны. Теперь у тебя больше маны.')

	user.mana(user.max_mp // 2)

fightable = True
def fight_use(user, reply, room):
	on_use(user, reply)

	return 0
