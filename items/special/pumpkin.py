from localizations import locale_manager
import random

name = locale_manager.get('items.special.pumpkin.phrase_1')
description = (
	locale_manager.get('items.special.pumpkin.phrase_2')
)

price = 3

fightable = True
strengthoff = True
disposable = True

def fight_use(user, reply, room):
	reply(locale_manager.get('items.special.pumpkin.phrase_3'))

	user.make_damage(0, 20, reply, name=locale_manager.get('items.special.pumpkin.phrase_4'))

	if user.dead:
		return 0
	
	return random.randint(50, 70)
