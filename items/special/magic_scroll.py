import random

name = 'Магический свиток'

description = (
	'На этом свитке записанно какое-то заклинание'
)

mp_cost = 100

price = 300
fightable = True
disposable = True


def fight_use(user, reply, room):

	if user.mp >= mp_cost:
		reply('Чпок!')
		user.mp -= mp_cost

		if random.random() < 0.25:
			reply(
				'Ты непонял как это случилось, '
				'но ты превратился в лягушку.\n\n'
				'Ну что, попрыгали искать принцессу.'
				'Надеюсь она не в другом замке'
			)

			user.reborn(reply)

		else:
			reply(
				'Ты превратил противника в лягушонка.\n'
				'Посмотри как он мило прыгает отсюда.'
			)

			user.won(reply)

	else:
		reply('А маны то не хватает!')
	return 0
