from constants import *

name = 'Черно-белое зелье'

description = (
	'Пробирка с каким-то черно-белым зельем.'
)

price = 100
shop_count = 2

usable = True
disposable = True

def on_use(user, reply):
	reply('Это оказалось зелье ПЕРЕМЕН. Ты поменял местами ману и жизнь.')

	user.hp, user.mp = user.mp, user.hp
	user.heal(0)
	user.mana(0)

fightable = True
def fight_use(user, reply, room):
	on_use(user, reply)

	return 0
