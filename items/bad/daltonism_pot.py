import items.itemloader as itemloader
from utils.potions import get_potion_color
from utils.potions import DALTONISM_POT

name = get_potion_color(itemloader.get_user(), DALTONISM_POT) + ' зелье'

description = 'Пробирка с каким-то зельем.'

price = 100
shop_count = 1

usable = True
disposable = True

def on_use(user, reply):
	if user.has_tag('daltonism'):
		user.remove_tags('daltonism')
		reply('Ты снова видишь цвет! Правда корридор все такой же серый и беспросветный..')
	else:
		user.add_tag('daltonism')
		reply('Это оказалось зелье дальтонизма. Что могу сказать.. «Клин клином вышибают» — вдруг поможет?')


fightable = True
def fight_use(user, reply, room):
	on_use(user, reply)

	return 0
