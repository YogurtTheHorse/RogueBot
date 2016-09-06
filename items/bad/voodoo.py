
name = 'кукла вуду'

description = ('небольшая тряпичная кукла, говорят, в умелых руках она творит чудеса')

price = 50

def on_room(user, reply, room):	
	reply('У вас закололо в груди')
	user.make_damage(20,30, reply, death=false)
	user.defence -= 5
