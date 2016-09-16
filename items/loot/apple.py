from constants import *

name = 'Яблочко'

description = (
	'Зелененькое.'
)

price = 50

usable = True
disposable = True

def on_use(user, reply):
	reply('Приятно.')

	user.hp = min(user.max_hp, user.hp + 50)

fightable = True
def fight_use(user, reply, room):
	on_use(user, reply)

	return 0

