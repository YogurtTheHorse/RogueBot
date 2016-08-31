from constants import *

name = 'Черное зелье'

description = (
	'Пробирка с каким-то черным зельем'
)

price = 100

usable = True
disposable = True

def on_use(user, reply):
	reply('Это оказалось зелье жизни. Теперь ты полностью здоров')

	user.hp = user.max_hp
