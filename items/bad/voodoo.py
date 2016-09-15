
name = 'Кукла вуду'

description = 'Небольшая тряпичная кукла, говорят, в умелых руках она творит чудеса.'

price = 50

def on_room(user, reply, room):	
	reply('У тебя закололо в груди.')
	user.make_damage(20,30, reply, death=False)
