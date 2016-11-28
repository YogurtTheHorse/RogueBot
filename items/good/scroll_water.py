from localizations import locale_manager
from constants import *
import random

name = locale_manager.get('items.good.scroll_water.phrase_1')

description = (
	locale_manager.get('items.good.scroll_water.phrase_2')
)


price = 100

fightable = True
disposable = True

def fight_use(user, reply, room):
	if 	user.use_mana(20):
		reply(locale_manager.get('items.good.scroll_water.phrase_3'))
		user.add_tag('wet_enemy')
		if random.random() < 0.1:
			user.add_tag('wet')
			reply(locale_manager.get('items.good.scroll_water.phrase_4'))
		return 100 - user.get_damage()
	else:
		reply(locale_manager.get('items.good.scroll_water.phrase_5'))
		user.add_item('good', 'scroll_water')
		return 0
