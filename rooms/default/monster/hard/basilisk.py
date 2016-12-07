from localizations import locale_manager
from random import randrange

name = locale_manager.get('rooms.default.monster_hard.basilisk.phrase_2')

hp = 135
damage_range =  ( 16, 25 )

coins = randrange(100, 150, 5)

loot = [ 'tooth_basilisk' ]


def enter(user, reply):
	msg = (
		locale_manager.get('rooms.default.monster_hard.basilisk.phrase_1'))
	reply(msg)
