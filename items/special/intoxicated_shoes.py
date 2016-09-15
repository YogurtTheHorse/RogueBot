name = 'Отравленные ботинки'
description = 'Довыпендривался.'

price = 0
iscursed = True

def on_room(user, reply, room):
	reply('Как же болят твои ноги.')
	user.make_damage(5, 10, reply, death=False)