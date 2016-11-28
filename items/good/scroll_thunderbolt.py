from localizations import locale_manager
from constants import *

name = locale_manager.get('items.good.scroll_thunderbolt.phrase_1')

description = (
	locale_manager.get('items.good.scroll_thunderbolt.phrase_2')
)

price = 200

fightable = True
disposable = True

def fight_use(user, reply, room):
	damage_non_wet = round((user.get_damage() + user.mana_damage)/2)*1.5 + 600
	damage_wet = round((user.get_damage() + user.mana_damage)/2)*3.5 + 1800
	if user.use_mana(50):
		reply(locale_manager.get('items.good.scroll_thunderbolt.phrase_3'))
		if user.has_tag('wet'):
			reply(locale_manager.get('items.good.scroll_thunderbolt.phrase_4'))
			user.make_damage(30, 50, reply, death=False, name=locale_manager.get('items.good.scroll_thunderbolt.phrase_5'))
		if user.has_tag('wet_enemy'):
			reply(locale_manager.get('items.good.scroll_thunderbolt.phrase_6'))
			return damage_wet - user.get_damage()
		else:
			return damage_non_wet - user.get_damage()
	else:
		reply(locale_manager.get('items.good.scroll_thunderbolt.phrase_7'))
		user.add_item('good', 'scroll_thunderbolt')
	
	return 0
