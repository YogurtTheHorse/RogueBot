from localizations import locale_manager
from constants import *

name = locale_manager.get('rooms.default.monster_medium.rabbit.phrase_1')

hp = 250
element = NONE
damage_range = ( 1, 3 )

coins = 3

loot = [ ]

def enter(user, reply):
	reply(locale_manager.get('rooms.default.monster_medium.rabbit.phrase_2'), photo='BQADAgAD8QgAAmrZzgdh94MU_Y8fegI')
