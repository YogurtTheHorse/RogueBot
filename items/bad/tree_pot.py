from constants import *

name = 'Коричневое зелье'

description = (
	'Пробирка с каким-то зельем'
)

price = 100
usable = True
disposable = True

def on_use(user, reply):
	reply('Теперь ты Дерево.', [ ])

	user.reborn(reply, 'Деревья ничего не делают', name='Дерево')
