from localizations import locale_manager
import random

name = locale_manager.get('items.neutral.bullet.phrase_1')

price = 2

description = (
	locale_manager.get('items.neutral.bullet.phrase_2')
)

fightable = True
disposable = True

def fight_use(user, reply, room):
	reply(locale_manager.get('items.neutral.bullet.phrase_3'))
	
	return 0