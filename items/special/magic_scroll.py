import random

name = 'Магический свиток'

description = (
	'На этом свитке записанно какое-то заклинание.'
)

mp_cost = 100

price = 300
fightable = True
disposable = True


def can_use(user, reply, room):
	return random.random() > 0.25 and room.code_name != 'doctor_who' and room.room_type != 'boss'


def fight_use(user, reply, room):
	if user.mp >= mp_cost:
		reply('Чпок!')
		user.mp -= mp_cost

	else:
		reply('А маны то не хватает!')

	return 0


def success(user, reply, room):
	reply(
		'Ты превратил противника в лягушонка.\n'
		'Посмотри как он мило прыгает отсюда.'
	)

	user.won(reply)


def failure(user, reply, room):
	if room.room_type != 'boss':
		reply(
			'Ты непонял как это случилось, '
			'но ты превратился в лягушку.\n\n'
			'Ну что, попрыгали искать принцессу. '
			'Надеюсь она не в другом замке.'
		)

		user.reborn(reply, 'Ква', name='Лягушка')

	else:
		reply('К счастью Магический свиток не сработал и ты не превратился в лягушку.')
	