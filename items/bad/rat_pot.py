from localizations import locale_manager
import items.itemloader as itemloader
from utils.potions import get_potion_color
from utils.potions import RAT_POT

name = get_potion_color(itemloader.get_user(), RAT_POT) + locale_manager.get('items.bad.rat_pot.phrase_1')

description = locale_manager.get('items.bad.rat_pot.phrase_2')

price = 100
usable = True
disposable = True

def on_use(user, reply):
	if user.race != 'rat':
		reply(locale_manager.get('items.bad.rat_pot.phrase_3'))
		user.race = 'rat'
	else:
		reply(locale_manager.get('items.bad.rat_pot.phrase_4'))
		user.race = 'human'
