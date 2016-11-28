from localizations import locale_manager
from localizations import locale_manager
name = locale_manager.get('items.pets.homeless.phrase_1')
description = ''
price = 0

def get_damage_bonus(user, reply):
	if user.has_item('whisky'):
		reply(locale_manager.get('items.pets.homeless.phrase_2'))
		return 11
	else:
		reply(locale_manager.get('items.pets.homeless.phrase_3'))
	return 0

def get_dice_bonus(user, reply):
	if user.has_item('whisky'):
		reply(locale_manager.get('items.pets.homeless.phrase_4'))
		return 7
	else:
		reply(locale_manager.get('items.pets.homeless.phrase_5'))
		return 0

def on_room(user, reply, room):
	if room.room_type == 'monster' and room.hp > 120:
		reply(locale_manager.get('items.pets.homeless.phrase_6'))
		user.remove_item('whisky')
		user.pet_gone()
	elif user.has_item('whisky'):
		reply(locale_manager.get('items.pets.homeless.phrase_7'))
