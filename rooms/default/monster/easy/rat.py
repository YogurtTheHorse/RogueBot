from localizations import locale_manager
from constants import *

name = locale_manager.get('rooms.default.monster_easy.rat.phrase_1')

hp = 20
element = NONE
damage_range =  ( 2, 4 )

coins = 7

loot = [ 'rat_tooth' ]

def enter(user, reply):
	if user.has_aura(AURA_BUDDHA):
		reply(locale_manager.get('rooms.default.monster_easy.rat.phrase_2'))
		user.won(reply)
	else:
		reply(locale_manager.get('rooms.default.monster_easy.rat.phrase_3'), photo='BQADAgADFgkAAmrZzgfs5OH3R2C_1wI')
