from localizations import locale_manager
name = 'Мазь "Звёздочка"'
description = locale_manager.get('items.loot.vietnam_star.phrase_1')
price = 300

usable = True
disposable = True

def on_use(user, reply):
	reply(locale_manager.get('items.loot.vietnam_star.phrase_2'))

	user.heal(25)

	user.buffs = [ b for b in user.buffs if not b.is_negative() ]