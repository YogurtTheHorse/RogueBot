from localizations import locale_manager
name = locale_manager.get('items.special.good_spoon.phrase_3')
description = (
	locale_manager.get('items.special.good_spoon.phrase_4')
)

price = 3

usable = True
def on_use(user, reply):
	reply(locale_manager.get('items.special.good_spoon.phrase_5'))
	if user.get_mana_damage() < 150:
		reply(
			locale_manager.get('items.special.good_spoon.phrase_1'))
	else:
		reply(
			locale_manager.get('items.special.good_spoon.phrase_2'))
		reply(locale_manager.get('items.special.good_spoon.phrase_6'))