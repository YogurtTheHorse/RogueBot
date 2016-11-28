import random
from localizations import locale_manager

name = locale_manager.get('items.loot.mechmod.phrase_1')
description = locale_manager.get('items.loot.mechmod.phrase_2')

price = 15
usable = True
fightable = True
disposable = True

def fight_use(user, reply, room):
	if random.random() < 0.3:
		reply(locale_manager.get('items.loot.mechmod.phrase_3'))
		user.leave(reply)
	else:
		reply(locale_manager.get('items.loot.mechmod.phrase_4'))

	return 0

def on_use(user, reply):
	reply(locale_manager.get('items.loot.mechmod.phrase_5'))

	user.defence -= 20
