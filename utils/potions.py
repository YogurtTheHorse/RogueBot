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
		locale_manager.get('gray', user.lang),
		locale_manager.get('black', user.lang),
		locale_manager.get('white', user.lang),
		locale_manager.get('yellow', user.lang),
		locale_manager.get('rainbow', user.lang),
		locale_manager.get('brown', user.lang),
		locale_manager.get('red', user.lang),
		locale_manager.get('pink', user.lang),
		locale_manager.get('azure', user.lang)
	]

	if user.has_tag('daltonism') or pot_num >= len(colors):
		return colors[0]

	seed = user.get_session_seed()
	seed += pot_num

	return colors[seed % len(colors)]
