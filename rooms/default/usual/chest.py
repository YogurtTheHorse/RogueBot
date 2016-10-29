from constants import *
import items.itemloader as itemloader
import itertools
import random

name = 'Сундук'

actions = ['Открыть сундук', 'Уйти']

TYPES_OF_ITEMS = [ 'bad', 'good', 'neutral' ]


def get_actions(user):
	return actions


def enter(user, reply):
	reply('Ты заходишь в комнату и видишь сундук.\nОбычный сундук', photo='BQADAgADCQkAAmrZzgfwfl33PblsWQI')


def action(user, reply, text):
	if text == actions[0]:
		reply(
			'Ты подходишь к сундуку...\n'
			'...\n'
			'...\n'
			'...\n'
			'...\n'
			'...\n'
			'Поднимаешь крышку\n'
		)

		random_number = random.random();

		if random_number < 0.33:
			reply('Пусто.\nОчень жаль. Повезет в следующий раз.')

		elif random_number < 0.66:
			coins = random.randrange(2, 5, 1)

			reply('Яркий свет ослепил тебя. В сундуке ты нашел немного монет.')
			for _ in itertools.repeat(None, coins):
				user.add_item('neutral', 'coin')

		else:
			item_type, item_name, item = __random_item()

			reply('В сундуке был {}'.format(item.name))
			user.add_item(item_type, item_name)

	user.leave(reply)


def __random_item():
	items = list(map(itemloader.load_random_item, TYPES_OF_ITEMS))

	item_type, item_name = random.choice(items)
	item = itemloader.load_item(item_name, item_type)

	return (item_type, item_name, item)
