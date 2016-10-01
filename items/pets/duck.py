from constants import DUCK_STICKER

name = 'Утка'
description = ''
price = 0

def on_room(user, reply, room):
	reply('Кря-кря!')

def get_damage_bonus(user, reply):
	reply('Утка крякает прямо врагу в нос.', photo=DUCK_STICKER)
	return 6