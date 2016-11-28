from localizations import locale_manager
from constants import *

name = locale_manager.get('items.bad.gum.phrase_2')

description = (
	locale_manager.get('items.bad.gum.phrase_1'))

charisma = -1
price = 10
tags = ['hair']

def on_buy(user, reply):
	if user.get_mana_damage() < SMART_LEVEL:
		reply(locale_manager.get('items.bad.gum.phrase_3'))
	else:
		charisma = 0
		reply(locale_manager.get('items.bad.gum.phrase_4'))
