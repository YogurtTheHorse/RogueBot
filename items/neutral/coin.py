from localizations import locale_manager
import random

name = locale_manager.get('items.neutral.coin.phrase_3')

price = 1

description = (
	locale_manager.get('items.neutral.coin.phrase_1'))

def get_dice_bonus(user, reply):
	if random.random() <= 0.1:
		txt = (
			locale_manager.get('items.neutral.coin.phrase_2'))
		reply(txt)

		return 1

	return 0