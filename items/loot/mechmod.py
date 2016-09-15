import random
name = 'Мехмод'
description = 'Вы чувствуете, как подворачиваются ваши штаны.'

price = 15
usable = True
fightable = True
disposable = True

def fight_use(user, reply, room):
	if random.random() < 0.3:
		reply('Все исчезло в дыму. Ты очутился в коридоре.')
		user.leave(reply)
	else:
		reply('Пых-пых.')

	return 0

def on_use(user, reply):
	reply('Ты ничего не видишь.')

	user.defence -= 20
