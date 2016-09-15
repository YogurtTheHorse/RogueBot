name = 'Собачка'
description = ''
price = 0

def on_room(user, reply, room):
	reply('Гав-гав!')

def get_damage_bonus(user, reply):
	reply('Собака кусает врага за зад.')
	return 16