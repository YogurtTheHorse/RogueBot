from constants import *

name = 'Жвачка'

description = (
	'Розовая жвачка со вкусом клубники. '
	'Ну хоть пожуешь чего-нибудь.'
)

charisma = -1
price = 10
tags = ['hair']

def on_buy(user, reply):
	if user.get_mana_damage() < SMART_LEVEL:
		reply('Надувать пузырь не стоило — жвачка застряла в волосах, а парикмахера ты тут вряд ли найдешь.')
	else:
		charisma = 0
		reply('А ты оказался достаточно умен, чтобы не запутать жвачку в волосах.')
