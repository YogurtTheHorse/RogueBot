from localizations import locale_manager
name = locale_manager.get('items.good.mage_stick.phrase_2')
description = (
	locale_manager.get('items.good.mage_stick.phrase_1'))

price = 100
mana_damage = 20
fightable = True

def fight_use(user, reply, room):
	reply(locale_manager.get('items.good.mage_stick.phrase_3'))

	user.remove_item_by_name(name)

	return 5