from localizations import locale_manager

MP_POT = 0
HP_POT = 1
HOMELESS_POT = 2
STONE_POT = 3
RAT_POT = 4
TREE_POT = 5
DALTONISM_POT = 6

def get_potion_color(user, pot_num):
	if user is None:
		return 'Gray'

	colors = [
		locale_manager.get('items.potions.gray', user.lang),
		locale_manager.get('items.potions.black', user.lang),
		locale_manager.get('items.potions.white', user.lang),
		locale_manager.get('items.potions.yellow', user.lang),
		locale_manager.get('items.potions.rainbow', user.lang),
		locale_manager.get('items.potions.brown', user.lang),
		locale_manager.get('items.potions.red', user.lang),
		locale_manager.get('items.potions.pink', user.lang),
		locale_manager.get('items.potions.azure', user.lang)
	]

	if user.has_tag('daltonism') or pot_num >= len(colors):
		return colors[0]

	seed = user.get_session_seed()
	seed += pot_num

	return colors[seed % len(colors)]
