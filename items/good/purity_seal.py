from localizations import locale_manager
from constants import *

name = locale_manager.get('items.good.purity_seal.phrase_1')

description = (locale_manager.get('items.good.purity_seal.phrase_2'))

price = 50

defence = 1

def on_pray(user, reply, god):
	if god == EMPEROR_NUM:
		user.gods_level[EMPEROR_NUM] += 1