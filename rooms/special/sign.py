import random
import rooms.roomloader as roomloader

name = 'Распутье'

room_type = 'other'

def get_actions(user):
	rooms = user.get_room_temp('rooms')

	actions = [ ]

	for room_type, room_name in rooms:
		loaded_room = roomloader.load_room(room_name, room_type)
		actions.append(loaded_room.name)

	return actions

def enter(user, reply):
	rooms = [  ]

	while len(rooms) < 3:
		rm = roomloader.get_next_room()
		if rm[1] != 'empty':
			rooms.append(rm)


	user.set_room_temp('rooms', rooms)

def action(user, reply, text):
	rooms = user.get_room_temp('rooms')
	for room_type, room_name in rooms:
		loaded_room = roomloader.load_room(room_name, room_type)
		if loaded_room.name == text:
			if random.random() < 0.1:
				reply('Что-то пошло не так, ты увидел фезку пролетающую у тебя над головой. Ощущения будто был нарушен межпространственный континиум.')
				user.open_room(reply)
			else:
				user.open_room(reply, room_type, room_name)
			return

	reply('Такого выбора тебе не давали')

