from localizations import locale_manager
from constants import *

name = locale_manager.get('items.good.swp_pot.phrase_1')

description = (
	locale_manager.get('items.good.swp_pot.phrase_2')
)

price = 100
shop_count = 2

usable = True
disposable = True

def on_use(user, reply):
	reply(locale_manager.get('items.good.swp_pot.phrase_3'))

	user.hp, user.mp = user.mp, user.hp
	user.heal(0)
	user.mana(0)

fightable = True
def fight_use(user, reply, room):
	on_use(user, reply)

	return 0
