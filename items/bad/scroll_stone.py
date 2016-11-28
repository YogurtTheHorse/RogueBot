from localizations import locale_manager
from constants import *

name = locale_manager.get('items.bad.scroll_stone.phrase_1')

description = (
	locale_manager.get('items.bad.scroll_stone.phrase_2')
)

price = 200

fightable = True
disposable = True

def fight_use(user, reply, room):
	if user.use_mana(50):
		reply(locale_manager.get('items.bad.scroll_stone.phrase_3'))
		user.make_damage(50, 100, reply, death=True, name=locale_manager.get('items.bad.scroll_stone.phrase_4'))
	else:
		reply(locale_manager.get('items.bad.scroll_stone.phrase_5'))
		user.add_item('bad', 'scroll_stone')
	return 0
