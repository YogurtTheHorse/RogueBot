name = 'Какой-то мужчина'

ASK = 'Ты носишь двуручник за спиной? Ты в каком фильме это видел?'
CAN_I_HELP = '— Может, тебе помочь?'
HELP = 'Помочь'
WAIT = 'Подождать'

def enter(user, reply):
	reply(
		'Вы видите мужчину, у которого седые волосы, желтые кошачьи глаза и 2 меча за спиной.\n'
		'Завидев вас, он пытается достать меч, судя по всему, серебрянный.'
	)
	user.set_room_temp('question', 'first')
	user.set_room_temp('cnt', 0)

def action(user, reply, text):
	question = user.get_room_temp('question', def_val='first')

	cnt = user.get_room_temp('cnt', 0) + 1
	user.set_room_temp('cnt', cnt)
	if text == ASK:
		reply('У мужчины глаза заливаются слезами, и он в истерике убегает из комнаты. Что это было?')
		user.leave(reply)
	elif text == CAN_I_HELP:
		reply('— Не надо, я сам! Я ведьмак, или ты?!')
		user.set_room_temp('question', 'third')
	elif text == HELP:
		reply(
			'Вы подходите к мужчине, с невозмутимым лицом достаете меч из его ножен на спине и отдаете '
			'его ему в руки, после чего уходите, сдерживая желание засмеяться'
		)
		user.leave(reply)
	else:
		reply('— Сейчас достану, подожди...')
		if cnt > 1:
			user.set_room_temp('question', 'second')

def get_actions(user):
	question = user.get_room_temp('question', def_val='first')

	if question == 'first':
		return [ WAIT, ASK ]
	elif question == 'second':
		return [ CAN_I_HELP, ASK ]
	else:
		return [ HELP, ASK ]