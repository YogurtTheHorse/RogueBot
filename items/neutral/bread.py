import random

name = 'Буханка хлеба'

price = 16

description = (
	'Свежий, теплый и мягкий. Разбирай'
)

fightable = True
disposable = True

def fight_use(user, reply, room):
	if room.code_name == 'duck':
		reply('Пока утка ела крошки, ты свернул ей шею. Так держать!')
		user.won(reply)

		return 0
	else:
		reply('Ты раскрошил хлеб. Зачем?')

		return 0