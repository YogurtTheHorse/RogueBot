from constants import *

name = 'Желтое зелье'

description = (
	'Пробирка с каким-то зельем. Какой-то подозрительный цвет...'
)

price = 100
usable = True
disposable = True

def on_use(user, reply):
	reply('Теперь ты Бомж... Впрочем, в нашей игре нет классового деления, так что ничего не меняется.')
