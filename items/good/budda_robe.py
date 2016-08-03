from constants import *

name = 'Роба Монаха'

description = (
	'Оранжевая роба какого-то монаха, который продал мне ее, чтобы купить еды. '
	'Некоторые монстры уважают Буддистов и не трогают их.'
)

aura = 'peace'
price = 150

def on_pray(user, reply, god):
	if god == BUDDHA:
		user.gods_level[BUDDHA_NUM] += 1
		