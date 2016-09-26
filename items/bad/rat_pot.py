import items.itemloader as itemloader
from utils.potions import get_potion_color
from utils.potions import RAT_POT

name = get_potion_color(itemloader.get_user(), RAT_POT) + ' зелье'

description = 'Пробирка с каким-то зельем.'

price = 100
usable = True
disposable = True

def on_use(user, reply):
	if user.race != 'rat':
		reply('Теперь ты Крыса.')
		user.race = 'rat'
	else:
		reply('ФУХ. ВСЕ БЫЛО ТАКИМ БОЛЬШИМ.')
		user.race = 'human'
