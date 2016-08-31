from constants import *

name = 'Зеленое зелье'

description = (
	'Пробирка с каким-то зеленым зельем'
)

price = 100
usable = True
disposable = True

def on_use(user, reply):
	reply('Теперь ты Дерево.', [ ])

	user.reborn(reply, 'Деревья ничего не делают')
