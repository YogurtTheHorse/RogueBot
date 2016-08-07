import random

name = 'Буханка хлеба'

price = 16

description = (
	'Свежий, теплый и мягкий. Разбирай'
)

fightable = True

def fight_use(user, reply, room):
	reply('Ты раскрошил хлеб. Зачем?')
	
	return 0