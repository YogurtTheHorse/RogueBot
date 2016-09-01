name = 'Назгул'

hp = 100
damage_range = ( 10, 15 )

coins = 0

loot = [ ]


def enter(user, reply):

	reply('ЭЙ, Приятель! Ты случайно историей не ошибся?')

	if user.darklord_level < 5:
		reply('*{} обиженно уходит'.format(name))
		user.leave(reply)

	else:
		# user.darklord_level += 2
		reply(
			'*Из-под капюшона послышалось шипение*\n'
			'Ой-ой! Кажется он не в духе!'
			'Может решим все по хорошему?'
		)