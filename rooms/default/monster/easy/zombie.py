from localizations import locale_manager
from constants import *
from random import randrange

name = locale_manager.get('rooms.default.monster_easy.zombie.phrase_2')
element = DEAD
hp = 20
damage_range = (0, 2)

coins = randrange(0, 5, 1)

loot = [ ]


def enter(user, reply):
	reply(
		locale_manager.get('rooms.default.monster_easy.zombie.phrase_1'),
		photo=ZOMBIE_STICKER
	)