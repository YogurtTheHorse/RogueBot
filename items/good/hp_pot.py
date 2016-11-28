from localizations import locale_manager
import items.itemloader as itemloader
from utils.potions import get_potion_color
from utils.potions import HP_POT

name = get_potion_color(itemloader.get_user(), HP_POT) + locale_manager.get('items.good.hp_pot.phrase_1')

description = locale_manager.get('items.good.hp_pot.phrase_2')

price = 100
shop_count = 2

usable = True
disposable = True

def on_use(user, reply):
	reply(locale_manager.get('items.good.hp_pot.phrase_3'))

	user.hp = user.max_hp

fightable = True
def fight_use(user, reply, room):
	on_use(user, reply)

	return 0
