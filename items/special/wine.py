import random

name = 'Винцо'

description = (
	'Бутылка отличного вина. Немного испачкана в иле. '
	'Божественный вкус.'
)

price = 300
fightable = True
disposable = True


def can_use(user, reply, room):
	reply('ЗА ВДВ!')

	return random.random() > 0.3 and room.code_name != 'doctor_who' and room.room_type != 'boss'


def success(user, reply, room):
	reply('Противник попятился назад. Это победа!')
	user.won(reply)


def failure(user, reply, room):
	reply('Это было больно.')

	if room.room_type != 'boss':
		user.death(reply, reason=name)

	else:
		reply('Но к счастью ты не пострадал.')
