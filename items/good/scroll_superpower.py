from constants import *
import random

name = 'Супер свиток'

description = (
	'Только лишь взглянув на него, твои мускулы увеличились. Ты хочешь кого-то ударить.'
)

price = 500

fightable = True
disposable = True

def fight_use(user, reply, room):
	if user.use_mana(100):
		reply('Твои руки увеличиваются и ты со всей силы бьешь врагу в лицо!')
		return user.get_damage()*3
	else:
		reply('Недостаточно маны')
		user.add_item('good', 'scroll_superpower')
		return 0
