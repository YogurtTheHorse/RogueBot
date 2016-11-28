from localizations import locale_manager
from constants import *

name = locale_manager.get('items.good.christ.phrase_2')

description = (
	locale_manager.get('items.good.christ.phrase_1'))

tags = [ 'wine' ]
price = 150

def on_pray(user, reply, god):
	if god == JESUS_NUM:
		user.gods_level[JESUS_NUM] += 1
