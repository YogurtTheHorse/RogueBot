import random

name = 'Ктулху'

hp = 575900
damage_range = ( 150, 250 )

coins = random.randrange( 1000, 100000, 1 )

def on_die(user, reply):
	msg = (
		'Ктулху обронил одно из своих щупалец и покинул поле боя.\n'
		'В этот раз ты одержал победу над ним, но не забывай -- Боги бессмертны.'
	)

	reply(msg)