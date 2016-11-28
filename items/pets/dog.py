from localizations import locale_manager
from localizations import locale_manager
name = locale_manager.get('items.pets.dog.phrase_1')
description = ''
price = 0

def on_room(user, reply, room):
	reply(locale_manager.get('items.pets.dog.phrase_2'))

def get_damage_bonus(user, reply):
	reply(locale_manager.get('items.pets.dog.phrase_3'))
	return 16