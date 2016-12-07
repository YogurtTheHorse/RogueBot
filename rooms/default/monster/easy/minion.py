from localizations import locale_manager
from constants import MINION_STICKER
from random import randrange

name = locale_manager.get('rooms.default.monster_easy.minion.phrase_2')
hp = 23
damage_range = ( 1, 4 )

coins = randrange(5, 10, 2)

loot = [ 'banana' ]


def enter(user, reply):
	reply(
		locale_manager.get('rooms.default.monster_easy.minion.phrase_1'),
		photo=MINION_STICKER
	)