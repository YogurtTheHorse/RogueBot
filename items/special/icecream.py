from localizations import locale_manager
import random 

name = locale_manager.get('items.special.icecream.name')

description = (
	locale_manager.get('items.special.icecream.phrase_1')
)

price = 30
tags = [ 'ice' ]
disposable = True

fightable = True

def fight_use(user, reply, room):
	reply(locale_manager.get('items.special.icecream.phrase_2'))
	
	return 15