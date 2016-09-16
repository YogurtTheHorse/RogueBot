import random

name = 'Пуля'

price = 2

description = (
	'Калибр в этой игре не важен, вот и знать тебе его не нужно.'
)

fightable = True
disposable = True

def fight_use(user, reply, room):
	reply('Ты выкинул пулю в противника. И зачем?')
	
	return 0