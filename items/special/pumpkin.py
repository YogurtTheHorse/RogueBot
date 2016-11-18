import random

name = 'Тыква'
description = (
	'Праздник к нам приходит, праздник к нам приходит!'
)

price = 3

fightable = True
strengthoff = True
disposable = True

def fight_use(user, reply, room):
	reply('Не фашисты, но гранату получат.')

	user.make_damage(0, 20, reply, name='Тыква')

	if user.dead:
		return 0
	
	return random.randint(50, 70)
