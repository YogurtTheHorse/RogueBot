from localizations import locale_manager
from constants import QUINQUEPEDE_STICKER

name = locale_manager.get('rooms.default.monster_easy.quinquepede.phrase_1')

hp = 50
damage_range =  ( 15, 30 )

coins = 30

loot = [ ]

def enter(user, reply):
	reply(locale_manager.get('rooms.default.monster_easy.quinquepede.phrase_2'), photo=QUINQUEPEDE_STICKER)
