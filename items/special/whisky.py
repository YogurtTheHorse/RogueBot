name = 'Виски'
description = 'Jack Daniel’s'
price = 100

def on_room(user, reply, room):
	if room.room_type == 'monster' and room.hp > 120:
		reply('Ну нахрен, ты это вообще видел? Я сваливаю. И виски заберу с собой!')
		user.remove_item('whisky')
	else:
		reply('Допивать будете?')