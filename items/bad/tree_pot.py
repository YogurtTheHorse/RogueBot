from localizations import locale_manager
from constants import TREE_STICKER

import items.itemloader as itemloader
from utils.potions import get_potion_color
from utils.potions import TREE_POT

name = get_potion_color(itemloader.get_user(), TREE_POT) + locale_manager.get('items.bad.tree_pot.phrase_1')

description = locale_manager.get('items.bad.tree_pot.phrase_2')

price = 100
usable = True
disposable = True

def on_use(user, reply):
	reply(locale_manager.get('items.bad.tree_pot.phrase_3'), [ ], photo=TREE_STICKER)

	user.reborn(reply, locale_manager.get('items.bad.tree_pot.phrase_4'), name=locale_manager.get('items.bad.tree_pot.phrase_5'))
