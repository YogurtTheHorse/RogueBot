import random
from constants import *

name = 'Банан'
description = (
	'Обычный спелый банан.'
)

price = 2
usable = True
fightable = True
disposable = True

def fight_use(user, reply, room):
	if room.code_name == 'minion':
		reply('С криками «BANANA!» миньон скрылся в неизвестно направлении.')
		user.won(reply)

		return 0
	else:
		if random.random() > 0.1:
			reply(
				'Ты поскользнулся на кожуре.\n'
				'Теперь будет синяк.'
			)
			user.make_damage(1, 2, reply, death=False)
		else:
			on_use(user, reply)
		
		return 0


def on_use(user, reply):
	reply('Ты чувствуешь себя лучше, теперь главное не поскользнуться на кожуре.')

	user.hp = min(user.max_hp, user.hp + 15)
