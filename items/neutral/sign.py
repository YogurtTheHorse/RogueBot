name = 'Указатель'
description = 'Указывает на дверь с указателем, который указывает.. Просто указывает.'

price = 300

usable = True

def on_use(user, reply):
	user.open_room(reply, 'special', 'sign')
