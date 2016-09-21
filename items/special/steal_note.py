name = 'Записка'
price = 1
description = 'Какой-то комок бумаги.'

usable = True

def on_use(user, reply):
	stealer = user.get_variable('stealer', 'none')

	thought = 'Кто же это мог быть..'
	if stealer != 'none':
		thought = 'Судя по почерку это мог быть только {0}!'.format(stealer)

	reply('Ты развернул комок бумаги прочитал:')
	reply('«Ахаха! Тебя обокрали!»\n{0}'.format(thought))