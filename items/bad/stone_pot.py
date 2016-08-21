from constants import *

name = 'Серое зелье'

description = (
	'Пробирка с каким-то серым зельем'
)

price = 100
usable = True

def on_use(user, reply):
	reply('Теперь ты Булыжник.', [ ])

	user.reborn(reply, 'Булыжник должен лежать')
