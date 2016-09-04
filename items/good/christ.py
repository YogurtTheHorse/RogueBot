from constants import *

name = 'Крестик'

description = (
	'Нательный крестик, который я нашел в одной из этих дверей. '
	'Не знаю, кто его носил, но он весь пропах вином.'
)

tags = [ 'wine' ]
price = 150

def on_pray(user, reply, god):
	if god == JESUS_NUM:
		user.gods_level[JESUS_NUM] += 1
