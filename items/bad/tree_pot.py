from constants import TREE_STICKER

import items.itemloader as itemloader
from utils.potions import get_potion_color
from utils.potions import TREE_POT

name = get_potion_color(itemloader.get_user(), TREE_POT) + ' зелье'

description = 'Пробирка с каким-то зельем.'

price = 100
usable = True
disposable = True

def on_use(user, reply):
	reply('Теперь ты Дерево.', [ ], photo=TREE_STICKER)

	user.reborn(reply, 'Деревья ничего не делают', name='Дерево')
