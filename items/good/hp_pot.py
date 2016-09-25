import items.itemloader as itemloader
from utils.potions import get_potion_color
from utils.potions import HP_POT

name = get_potion_color(itemloader.get_user(), HP_POT) + ' зелье'

description = 'Пробирка с каким-то зельем.'

price = 100
shop_count = 2

usable = True
disposable = True

def on_use(user, reply):
	reply('Это оказалось зелье жизни. Теперь ты здоровее чем мог бы быть.')

	user.hp = user.max_hp

fightable = True
def fight_use(user, reply, room):
	on_use(user, reply)

	return 0
