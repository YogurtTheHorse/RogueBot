from constants import *
from random import randrange

name = 'Зомби'
element = DEAD
hp = 20
damage_range = (0, 2)

coins = randrange(0, 5, 1)

loot = [ ]


def enter(user, reply):
	reply(
		'Откуда тут Зомби?\n'
		'Не уж то у нас тут некроманты завелись?\n'
		'Стыдоба то какая!!!',
		photo=ZOMBIE_STICKER
	)