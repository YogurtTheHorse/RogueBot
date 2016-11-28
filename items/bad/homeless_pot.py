from localizations import locale_manager
import items.itemloader as itemloader
from utils.potions import get_potion_color
from utils.potions import HOMELESS_POT

name = get_potion_color(itemloader.get_user(), HOMELESS_POT) + locale_manager.get('items.bad.homeless_pot.phrase_1')

description = locale_manager.get('items.bad.homeless_pot.phrase_2')

price = 100
usable = True
disposable = True

def on_use(user, reply):
	reply(locale_manager.get('items.bad.homeless_pot.phrase_3'))
