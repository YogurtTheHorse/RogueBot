
name = 'Пустой свиток'

description = (
	'В этом свите можно делать записи!\n'
	'Осталось только научиться.'
)

mp_cost = 50

price = 1000

usable = True
disposable = True


def on_use(user, reply):

	if user.has_item('tooth_basilisk'):

		if user.mp >= mp_cost:

			reply(
				'Ты наносишь какие-то загадочные символы на свиток\n'
				'Когда дописан последний символ, буквы вспихивают\n'
				'Кажется у тебя получилось сделать *Магический свиток*\n\n'
				'*Из инвентаря пропал зуб Василиска*'

			)

			user.remove_item('tooth_basilisk')
			user.mp -= mp_cost
			user.add_item('special', 'magic_scroll')

		else:
			reply('Не получилось.\n\n *Ты лишился Свитка и зуба Василиска*.')
			user.remove_item('tooth_basilisk')
			user.mp = 0

	else:
		reply('Молодец! Ты его испортил!')

