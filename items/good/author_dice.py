from constants import *

name = 'Игральная кость Рассказчика'

description = (
	'Игральная кость, которую мне отдал рассказчик по ненадобности. '
	'Он же рассказчик — зачем ему? Правда на ней всегда выпадает единица...'
)

price = 150

def get_dice_bonus(user, reply):
	return 1

def on_pray(user, reply, god):
	if god == AUTHOR_NUM:
		user.gods_level[AUTHOR_NUM] += 1
