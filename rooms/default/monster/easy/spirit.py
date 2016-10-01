from constants import *

name = 'Дух бесплотный'
element = DEAD
hp = 10
damage_range = (1, 5)

coins = 0

loot = []


def enter(user, reply):
	reply('Единение!', photo=GHOST_STICKER)