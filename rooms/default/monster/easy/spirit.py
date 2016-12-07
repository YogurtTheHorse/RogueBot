from localizations import locale_manager
from constants import *

name = locale_manager.get('rooms.default.monster_easy.spirit.phrase_1')
element = DEAD
hp = 10
damage_range = (1, 5)

coins = 0

loot = []


def enter(user, reply):
	reply(locale_manager.get('rooms.default.monster_easy.spirit.phrase_2'), photo=GHOST_STICKER)