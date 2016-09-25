import items.itemloader as itemloader
from utils.potions import get_potion_color
from utils.potions import MP_POT

name = get_potion_color(itemloader.get_user(), MP_POT) + ' зелье'

description = 'Пробирка с каким-то зельем.'

price = 100
shop_count = 3

usable = True
disposable = True

def on_use(user, reply):
	reply('Это оказалось зелье маны. Теперь у тебя больше маны.')

	user.mana(user.max_mp // 2)

fightable = True
def fight_use(user, reply, room):
	on_use(user, reply)

	return 0
