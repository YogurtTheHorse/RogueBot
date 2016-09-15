from constants import *

name = 'Белое зелье'

description = (
	'Пробирка с каким-то зельем.'
)

price = 100
usable = True
disposable = True

def on_use(user, reply):
	reply('Теперь ты Булыжник.', photo='BQADAgAD8gADDLXzAxLUH2ng6NIiAg')

	user.reborn(reply, 'Булыжник должен лежать', name='Булыжник')
