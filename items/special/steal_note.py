import items.itemloader as itemloader

context = itemloader.get_context()

name = 'Записка'
price = 1
description = 'Какой-то комок бумаги.'

usable = True

def on_use(user, reply):
	stealer = user.get_variable('stealer', 'none')

	thought = 'Кто же это мог быть..'
	if stealer != 'none':
		thought = 'Судя по почерку это мог быть только {0}!'.format(stealer)
	else:
		thought = 'Судя по почерку это мог быть только {0}! У тебя украли {1}.'.format(context['stealer'], context['item_name'])

	reply('Ты развернул комок бумаги прочитал:')
	reply('«Ахаха! Тебя обокрали!»\n{0}'.format(thought))
