import random

name = 'Ктулху'

hp = 575900
damage_range = ( 150, 250 )

coins = random.randrange( 1000, 251000, 1 )


def skill_preparing(user, reply, boss):
  msg = (
    'Ты услышал громыхающее рычание и увидел, что Ктулху замахивается на тебя всеми своими щупальцами.'
  )

  reply(msg, photo='BQADAgAD_AgAAmrZzge-xwd2a6LXzAI')


def on_die(user, reply):
	msg = (
		'Ктулху обронил одно из своих щупалец и покинул поле боя.\n'
		'В этот раз ты одержал победу над ним, но не забывай — Боги бессмертны.'
	)

	reply(msg)
