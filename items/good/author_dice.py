from localizations import locale_manager
from constants import *

name = locale_manager.get('items.good.author_dice.phrase_2')

description = (
	locale_manager.get('items.good.author_dice.phrase_1'))

price = 150

def get_dice_bonus(user, reply):
	return 1

def on_pray(user, reply, god):
	if god == AUTHOR_NUM:
		user.gods_level[AUTHOR_NUM] += 1
