from localizations import locale_manager
from localizations import locale_manager
name = locale_manager.get('items.pets.bear.phrase_1')
description = ''
price = 0

defence = 25

def on_room(user, reply, room):
	if room.room_type == 'monster':
		reply(locale_manager.get('items.pets.bear.phrase_2'))