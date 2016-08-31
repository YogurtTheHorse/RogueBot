from constants import *

name = 'Дух бесплотный'
element = DEAD
hp = 10
damage_range = (1, 5)

coins = 0

loot = [ 'unity' ]


def enter(user, reply):
	reply('Не прикаенно бродит по темным коридорам'.format(name))