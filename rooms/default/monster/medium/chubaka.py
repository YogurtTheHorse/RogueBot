from localizations import locale_manager
from constants import *

name = locale_manager.get('rooms.default.monster_medium.chubaka.phrase_1')

hp = 120
element = NONE
damage_range =  ( 16, 18 )

coins = 25

loot = [ 'laser_gun' ]

def enter(user, reply):
	reply(locale_manager.get('rooms.default.monster_medium.chubaka.phrase_2'), photo='BQADAgADyAgAAmrZzgd4ASvAJrnDtwI')

	if user.has_aura(AURA_BUDDHA):
		reply(locale_manager.get('rooms.default.monster_medium.chubaka.phrase_3'))
		user.leave(reply)
	elif user.rooms_count < 100:
		reply(locale_manager.get('rooms.default.monster_medium.chubaka.phrase_4'))
		user.leave(reply)