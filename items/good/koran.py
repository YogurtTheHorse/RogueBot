from constants import *

name = 'Коран'

description = (
	'Священная книга мусульман. Написана на арабском, поэтому я даже не брался за нее. '
	'Забирай, если хочешь. Бесплатно? Это же священная книжка! _Ты что?!_ '
)

price = 100

def on_pray(user, reply, god):
	if god == ALLAH_NUM:
		user.gods_level[ALLAH_NUM] += 1
