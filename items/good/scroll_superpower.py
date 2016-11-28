from localizations import locale_manager
from constants import *
import random

name = locale_manager.get('items.good.scroll_superpower.phrase_1')

description = (
	locale_manager.get('items.good.scroll_superpower.phrase_2')
)

price = 500

fightable = True
disposable = True

def fight_use(user, reply, room):
	if user.use_mana(100):
		reply(locale_manager.get('items.good.scroll_superpower.phrase_3'))
		return user.get_damage()*3
	else:
		reply(locale_manager.get('items.good.scroll_superpower.phrase_4'))
		user.add_item('good', 'scroll_superpower')
		return 0
