import random
import usermanager

name = 'Останки'

actions = [ 'Забрать себе', 'Уйти' ]

def get_actions(user):
	return actions

def enter(user, reply):
	users = list(usermanager.get_telegram_users())
	random.shuffle(users)

	user_id = None
	found_user = None

	for usr_id in users:
		usr = usermanager.get_user(usr_id)
		if usr.dead:
			user_id = usr_id
			found_user = usr
			break

	if found_user is not None:
		reply('Здесь лежат останки игрока {0}'.format(found_user.name))
		user.set_room_temp('items', found_user.items)
	else:
		reply('Здесь лежат останки лягушки. Воняет. Ты уходишь отсюда побыстрее.')
		user.leave(reply)


def action(user, reply, text):
	if text == actions[0]:
		items = user.get_room_temp('items', def_val=[])
		if len(items) == 0:
			reply('У него ничего не было.')
		else:
			reply('Ты забрал его вещи.')
			for it in items:
				user.add_item(it[0], it[1])
	else:
		reply('Ты уходишь отсюда.')
		
	user.leave(reply)