from constants import *

name = 'Желтое зелье'

description = (
	'Пробирка с каким-то зельем. Какой подозрительный цвет...'
)

price = 100
usable = True
disposable = True

def on_use(user, reply):
	reply('Теперь ты Бомж... В прочем в нашей игре нет классового деления, так что ничего не меняется')
