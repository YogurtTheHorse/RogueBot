COLORS = [ 'Серое', 'Черное', 'Белое', 'Желтое', 'Радужное', 'Коричневое', 'Красное', 'Розовое', 'Лазуревое' ]

MP_POT = 0
HP_POT = 1
HOMELESS_POT = 2
STONE_POT = 3
RAT_POT = 4
TREE_POT = 5
DALTONISM_POT = 6

def get_potion_color(user, pot_num):
	if user is None:
		return COLORS[0]

	if user.has_tag('daltonism') or pot_num >= len(COLORS):
		return COLORS[0]

	seed = user.get_session_seed()
	seed += pot_num

	return COLORS[seed % len(COLORS)]
