import items.itemloader as itemloader
from utils.potions import get_potion_color
from utils.potions import STONE_POT

name = get_potion_color(itemloader.get_user(), STONE_POT) + ' зелье'

description = 'Пробирка с каким-то зельем.'

price = 100
usable = True
disposable = True

def on_use(user, reply):
	reply('Теперь ты Булыжник.', photo='BQADAgAD7wgAAmrZzgdNC04WtFQVSAI')

	user.reborn(reply, 'Булыжник должен лежать', name='Булыжник')
