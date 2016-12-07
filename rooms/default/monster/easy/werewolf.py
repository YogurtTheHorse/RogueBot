from localizations import locale_manager
from constants import WOLF_STICKER

name = locale_manager.get('rooms.default.monster_easy.werewolf.phrase_1')

hp = 35
damage_range =  ( 15, 23 )

coins = 21

loot = [ ]


def enter(user, reply):
	reply(locale_manager.get('rooms.default.monster_easy.werewolf.phrase_2'), photo=WOLF_STICKER)
