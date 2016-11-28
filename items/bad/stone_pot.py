from localizations import locale_manager
import items.itemloader as itemloader
from utils.potions import get_potion_color
from utils.potions import STONE_POT

name = get_potion_color(itemloader.get_user(), STONE_POT) + locale_manager.get('items.bad.stone_pot.phrase_1')

description = locale_manager.get('items.bad.stone_pot.phrase_2')

price = 100
usable = True
disposable = True

def on_use(user, reply):
	reply(locale_manager.get('items.bad.stone_pot.phrase_3'), photo='BQADAgAD7wgAAmrZzgdNC04WtFQVSAI')

	user.reborn(reply, locale_manager.get('items.bad.stone_pot.phrase_4'), name=locale_manager.get('items.bad.stone_pot.phrase_5'))
