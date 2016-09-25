import usermanager

name = 'Катапульта'

def enter(user, reply):
	msg = (
		'Указав имя отправителя ты сможешь запулить в него булыжником!\n\n'
		'Только скажи куда доставить посылку'
	)
	reply(msg)

	user.set_room_temp('question', 'first')

def get_actions(user):
	return [  ]

def action(user, reply, text):
	question = user.get_room_temp('question', def_val='first')

	if question == 'first':
		user.set_room_temp('goal_name', text)
		user.set_room_temp('question', 'second')
		reply('Теперь напечатай текст послания.')
	else:
		name = user.get_room_temp('goal_name', def_val='____')
		found_uid = 0
		found_usr = None

		for uid in usermanager.get_telegram_users():
			usr = usermanager.get_user(uid)
			if usr.name == name:
				found_uid = uid
				found_usr = usr
				break

		if found_usr is None:
			reply('Вашего адресата мы не нашли, но нашли кое-кого другого')
			found_usr = usermanager.random_user()

		reply('Отлично! Доставим в кратчайшие сроки.')

		if found_uid == user.uid:
			user.add_item('good', 'stone', {'message': text})
		else:
			found_usr.add_item('good', 'stone', {'message': text})
			usermanager.save_user(found_usr)

		user.leave(reply)
