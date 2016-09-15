name = 'Медведь'
description = ''
price = 0

defence = 25

def on_room(user, reply, room):
	if room.room_type == 'monster':
		reply('Медведь стоит перед врагом и защищает тебя.')