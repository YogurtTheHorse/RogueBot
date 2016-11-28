from localizations import locale_manager
import random
from constants import *

name = locale_manager.get('items.loot.banana.phrase_2')
description = (
	locale_manager.get('items.loot.banana.phrase_3')
)

price = 2
usable = True
fightable = True
disposable = True

def fight_use(user, reply, room):
	if room.code_name == 'minion':
		reply(locale_manager.get('items.loot.banana.phrase_4'))
		user.won(reply)

		return 0
	else:
		if random.random() > 0.1:
			reply(
				locale_manager.get('items.loot.banana.phrase_1'))
			user.make_damage(1, 2, reply, death=False)
		else:
			on_use(user, reply)
		
		return 0


def on_use(user, reply):
	reply(locale_manager.get('items.loot.banana.phrase_5'))

	user.hp = min(user.max_hp, user.hp + 15)
