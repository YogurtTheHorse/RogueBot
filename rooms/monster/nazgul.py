name = 'Назгул'

hp = 100
damage_range = ( 10, 15 )

coins = 130

loot = [ ]


def enter(user, reply):
	reply('Эй, Приятель! Ты случайно историей не ошибся?')

	if user.rooms_count < 75:
		reply('{} обиженно уходит'.format(name))
		user.leave(reply)

	else:
		reply(
			'*Из-под капюшона послышалось шипение*\n'
			'Ой-ой! Кажется он не в духе!'
			'Может решим все по хорошему?'
		)
