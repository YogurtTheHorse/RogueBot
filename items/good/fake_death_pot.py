from localizations import locale_manager
import random
from constants import *

name = locale_manager.get('items.good.fake_death_pot.phrase_1')

description = (
	locale_manager.get('items.good.fake_death_pot.phrase_2')
)

price = 100
shop_count = 2

disposable = True

fightable = True
def fight_use(user, reply, room):
	if random.random() > 0.5:
		reply(locale_manager.get('items.good.fake_death_pot.phrase_3'))
		user.leave(reply)
	else:
		reply(locale_manager.get('items.good.fake_death_pot.phrase_4'))
		user.death(reply, reason=name)

	return 0