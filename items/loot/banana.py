from constants import *

name = 'Банан'
description = (
	'Обычный спелый банан'
)

price = 2
usable = True
fightable = True


def fight_use(user, reply, room):
	if room.code_name == 'minion':
		reply('С криками "BANANA!" миньон скрылся в неизвестно направлении')
		user.remove_item_by_name(name)
		user.won(reply)

		return 0
	else:
		reply('Ты поскользнулся на кожуре\Теперь будет синяк')
		user.make_damage(1, 2, reply, death=False)
		user.remove_item_by_name(name)
		return 0


def on_use(user, reply):
	reply('Ты чувствуешь себя лучше, теперь главное не поскользнуться на кожуре')

	user.hp += 15
	user.remove_item_by_name(name)
