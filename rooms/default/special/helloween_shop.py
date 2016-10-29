import random
from items import itemloader
from utils import costumes

name = 'Зуллуинский магазин'

ACTIONS = [ 'Тыква', 'Костюм', 'Конфета' ]

def enter(user, reply):
	reply(
		'Какие-то странные бездедушки, черепа и прочая ересь.\n'
		'Рука невольно тянется к ручки двери, чтобы сбежать, но '
		'какая-та улыбчивая тварь пригласила тебя внутрь и предлагает тебе взять что-то одно, но зато *абсолютно* бесплатно.'
	)

	user.set_room_temp('costume', costumes.rand_costume_key())

def get_actions(user):
	return ACTIONS

def action(user, reply, text):
	if text == ACTIONS[0]:
		reply('Держи!', photo='BQADAgAD7QgAAmrZzgfDVlphbK6MlgI')
		user.add_item('special', 'pumpkin')
		user.leave(reply)
	elif text == 'Свечка':
		reply('Держи свечу, не обожгись!')
		user.add_item('special', 'candle')
		user.leave(reply)
	elif text == ACTIONS[1]:
		key = user.get_room_temp('costume', 'none')
		costume = costumes.get_costume(key)

		user.costume = key

		reply('Держи этот шикарный костюм!')
		reply('_Вы надеваете костюм {0}_'.format(costume['who']))
		reply(costume['description'])
	elif text == ACTIONS[2]:
		reply('Забирай, но не переедай!')

		user.add_item('special', 'candy')
	else:
		reply('Не понял сейчас')
		return

	user.leave(reply)
