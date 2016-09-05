READY = 'Подойти ближе'
ESCAPE = 'Уйти'
CLOSER = 'Подойти еще ближе'

name = 'Красотка'

def enter(user, reply):
	msg = ( 
		'Ты видишь огненную красотку\n'
		'Она улыбнулась тебе и поманила пальчиком к себе'
	)
	reply(msg)
	user.set_room_temp('question', 'first')

def action(user, reply, text):
	question = user.get_room_temp('question', def_val='first')

	if question == 'first':
		if text  == READY:
			reply('Вы подходите ближе, а красотка начинает раздеваться')
			user.set_room_temp('question', 'undress')
		else:
			reply('Красотка обиженно на вас смотрит')
			user.leave(reply)
	elif question == 'undress':
		if text == CLOSER:
			if user.has_item('christ'):
				reply(
					'ВНЕЗАПНО красотка исчезает.\n'
					'Вместо нее появляются три мужика в красном\n'
					'..\n'
					'НИКТО НЕ ОЖИДАЕТ ИСПАН...\n'
					'А, так ты из наших, держи, это тебе.\n'
					'Протягивает Винцо'
				)
				user.add_item('special', 'wine')
				user.leave(reply)
			else:
				msg = (
					'ВНЕЗАПНО красотка исчезает.\n'
					'Вместо нее появляются три мужика в красном\n'
					'..\n'
					'НИКТО НЕ ОЖИДАЕТ ИСПАНСКУЮ ИНКВИЗИЦИЮ!\n'
					'На костёр неверного!'
				)
				reply(msg)
				user.death(reply, reason='Инквизиция')
		else:
			reply('Красотка обиженно на вас смотрит')
			user.leave(reply)

def get_actions(user):
	question = user.get_room_temp('question', def_val='first')
	ans = [ ]

	if question == 'first':
		ans = [ READY, ESCAPE ]
	else:
		ans = [ CLOSER, ESCAPE]

	return ans
