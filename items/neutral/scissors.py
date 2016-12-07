from localizations import locale_manager
import random 

name = locale_manager.get('items.neutral.scissors.name')

description = (
	locale_manager.get('items.neutral.scissors.phrase_1')
)

price = 10
tags = [ 'scissors' ]

def get_damage_bonus(user, reply):
	if random.random() < 0.5:
		return 1
	else:
		reply(locale_manager.get('items.neutral.scissors.phrase_2'))
		user.make_damage(1, 2, reply, death=False)
		return 0