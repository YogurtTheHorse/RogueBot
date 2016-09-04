from constants import *

name = 'Радужное зелье'

description = (
	'Пробирка с каким-то зельем. Инетерсно...'
)

price = 100
usable = True
disposable = True

def on_use(user, reply):
	if user.race != RAT_RACE:
		reply('Теперь ты Крыса.')
		user.race = RAT_RACE
	else:
		reply('ФУХ. ВСЕ БЫЛО ТАКИМ БОЛЬШИМ')
		user.race = HUMAN
