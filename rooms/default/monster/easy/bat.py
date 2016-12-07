from localizations import locale_manager
from constants import *

name = locale_manager.get('rooms.default.monster_easy.bat.phrase_2')

hp = 15
element = NONE
damage_range =  ( 5, 7 )

coins = 12

loot = [ 'bat_wing' ]

def enter(user, reply):
	msg = (
		locale_manager.get('rooms.default.monster_easy.bat.phrase_1'))
	reply(msg, photo=BAT_STICKER)
