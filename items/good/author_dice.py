from constants import *

name = 'Игральная кость Рассказчика'

description = (
	'Игральная кость, которую мне отдал рассказчик по ненадобности. '
	'Он же рассказчик — зачем ему? Правда на ней всегда выпадает единица...'
)

dice_bonus = 1
price = 150

def on_pray(user, reply, god):
	if god == AUTHOR:
		user.gods_level[AUTHOR_NUM] += 1
