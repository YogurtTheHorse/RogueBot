import random 

name = "Ножницы"

description = (
	'Ножницы как ножницы. Только не порежься.'
)

price = 10
tags = [ 'scissors' ]

def get_damage_bonus(user, reply):
	if random.random() < 0.5:
		return 1
	else:
		reply('Ты порезался ножницами, красава.')
		user.make_damage(1, 2, reply, death=False)
		return 0