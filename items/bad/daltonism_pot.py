from localizations import locale_manager
import items.itemloader as itemloader
from utils.potions import get_potion_color
from utils.potions import DALTONISM_POT

name = get_potion_color(itemloader.get_user(), DALTONISM_POT) + locale_manager.get('items.bad.daltonism_pot.phrase_1')

description = locale_manager.get('items.bad.daltonism_pot.phrase_2')

price = 100
shop_count = 1

usable = True
disposable = True

def on_use(user, reply):
	if user.has_tag('daltonism'):
		user.remove_tags('daltonism')
		reply(locale_manager.get('items.bad.daltonism_pot.phrase_3'))
	else:
		user.add_tag('daltonism')
		reply(locale_manager.get('items.bad.daltonism_pot.phrase_4'))


fightable = True
def fight_use(user, reply, room):
	on_use(user, reply)

	return 0
