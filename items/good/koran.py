from localizations import locale_manager
from constants import *

name = locale_manager.get('items.good.koran.phrase_2')

description = (
	locale_manager.get('items.good.koran.phrase_1'))

price = 100

def on_pray(user, reply, god):
	if god == ALLAH_NUM:
		user.gods_level[ALLAH_NUM] += 1
