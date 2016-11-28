from localizations import locale_manager
from localizations import locale_manager
from constants import DUCK_STICKER

name = locale_manager.get('items.pets.duck.phrase_1')
description = ''
price = 0

def on_room(user, reply, room):
	reply(locale_manager.get('items.pets.duck.phrase_2'))

def get_damage_bonus(user, reply):
	reply(locale_manager.get('items.pets.duck.phrase_3'), photo=DUCK_STICKER)
	return 6