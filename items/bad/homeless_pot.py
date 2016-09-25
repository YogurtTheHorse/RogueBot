import items.itemloader as itemloader
from utils.potions import get_potion_color
from utils.potions import HOMELESS_POT

name = get_potion_color(itemloader.get_user(), HOMELESS_POT) + ' зелье'

description = 'Пробирка с каким-то зельем.'

price = 100
usable = True
disposable = True

def on_use(user, reply):
	reply('Теперь ты Бомж... Впрочем, в нашей игре нет классового деления, так что ничего не меняется.')
