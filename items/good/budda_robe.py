from localizations import locale_manager
from constants import *

name = locale_manager.get('items.good.budda_robe.phrase_2')

description = (
	locale_manager.get('items.good.budda_robe.phrase_1'))

aura = AURA_BUDDHA
price = 150

def on_pray(user, reply, god):
	if god == BUDDHA_NUM:
		user.gods_level[BUDDHA_NUM] += 1
		