from localizations import locale_manager
from constants import *

name = locale_manager.get('items.loot.apple.phrase_1')

description = (
	locale_manager.get('items.loot.apple.phrase_2')
)

price = 50

usable = True
disposable = True

def on_use(user, reply):
	reply(locale_manager.get('items.loot.apple.phrase_3'))

	user.hp = min(user.max_hp, user.hp + 50)

fightable = True
def fight_use(user, reply, room):
	on_use(user, reply)

	return 0

