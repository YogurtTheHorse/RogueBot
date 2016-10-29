import random
from items import itemloader

name = 'Караван Дварфов'

FIRST_ACTIONS = [ 'Закупиться', 'Заказать', 'Ограбить', 'Уйти' ]

def enter(user, reply):
	reply(
		'Ты открываешь дверь и видишь целый караван дварфов!\n'
		'К тебе подходит рыжебородый дварф в доспехах и начинает разговор:\n\n'
		'— Привет, Путник! Мы уже встречали тебя на просторах этого подземелья '
		'и привезли тебе то, что ты просил.. Ну постарались привезти..',
		photo='BQADAgADDwkAAmrZzgeuSKp_XxTj7wI'
	)

	user.set_room_temp('question', 'first')

	generate_items(user)
	generate_items_text(user, 'trade_items')
	generate_items_text(user, 'new_order_list')

def generate_items(user):
	items = [ ]
	order_list = user.get_variable('order_list', def_val=[ ])

	for i in range(10):
		item = order_list[i] if i < len(order_list) else None
		if item is None or random.random() > 0.9:
			typ = 'good'
			if i > 7:
				typ = 'neutral'
			item = itemloader.load_random_item(typ)

		while item in items:
			item = itemloader.load_random_item('good')

		items.append(item)

	user.set_room_temp('trade_items', items)
	user.set_room_temp('new_order_list', [ itemloader.load_random_item('good') for i in range(7) ])
	user.set_variable('order_list', [ ])

def generate_items_text(user, lst):
	trade_items = user.get_room_temp(lst, def_val=[ ])

	items =  [ itemloader.load_item(i[1], i[0]) for i in trade_items ]

	names = [ i.name for i in items ]
	descriptions = [ i.description for i in items if i is not None ]
	costs = [ i.price * 2 for i in items if i is not None ]

	user.set_room_temp(lst + '_names', names)
	user.set_room_temp(lst + '_descriptions', descriptions)
	user.set_room_temp(lst + '_costs', costs)

def get_actions(user):
	question = user.get_room_temp('question', def_val='first')
	
	if question == 'first':
		return FIRST_ACTIONS
	elif question == 'trade':
		return user.get_room_temp('trade_items_names') + [ 'Назад' ]
	elif question == 'order':
		return user.get_room_temp('new_order_list_names') + [ 'Назад' ]

def get_message(user, lst):
	names = user.get_room_temp(lst + '_names', [])
	descriptions = user.get_room_temp(lst + '_descriptions', [])
	costs = user.get_room_temp(lst + '_costs', [])

	msg = 'Вот, что у нас есть сегодня:\n\n'
	msg += '\n\n'.join([ '{0}\nЦена: {1}\n{2}'.format(name, costs[i], descriptions[i]) for i, name in enumerate(names) ])

	return msg

def buy(user, reply, name):
	names = user.get_room_temp('trade_items_names', def_val=[ ])
	costs = user.get_room_temp('trade_items_costs', def_val=[ ])
	trade_items = user.get_room_temp('trade_items', def_val=[ ])

	if name in names:
		ind = names.index(name)
		item = trade_items[ind]

		if user.paid(costs[ind]):
			user.add_item(trade_items[ind][0], trade_items[ind][1])
			costs[ind] *= 2
			user.set_room_temp('trade_items_costs', costs)

			reply('Забирай! Теперь {0} стоит *{1}*.'.format(name, costs[ind]))
		else:
			reply('Дварф ехидно улыбается и не отдает тебе вещь.\n«Нет денег — нет товара».')


		return True
	else:
		return False

def steal(user):
	trade_items = user.get_room_temp('trade_items', def_val=[ ])

	for i in trade_items:
		user.add_item(i[0], i[1])

def order(user, name):
	names = user.get_room_temp('new_order_list_names', [])
	descriptions = user.get_room_temp('new_order_list_descriptions', [])
	costs = user.get_room_temp('new_order_list_costs', [])

	if name in names:
		new_order_list = user.get_room_temp('new_order_list', def_val=[ ])
		ind = names.index(name)

		item = new_order_list[ind]

		del new_order_list[ind]
		del names[ind]
		del descriptions[ind]
		del costs[ind]

		user.set_room_temp('new_order_list', new_order_list)
		user.set_room_temp('new_order_list_names', names)
		user.set_room_temp('new_order_list_descriptions', descriptions)
		user.set_room_temp('new_order_list_costs', costs)

		order_list = user.get_variable('order_list', def_val=[ ])
		order_list.append(item)
		user.set_variable('order_list', order_list)

		return True
	else:
		return False

def leave(user, reply, with_army=False):
	user.leave(reply)
	if with_army:
		user.new_mission('caravan', 'army', path_len=25)
	else:
		user.new_mission('caravan', 'caravan')

def action(user, reply, text):
	question = user.get_room_temp('question', def_val='first')

	if question == 'first':
		if text == FIRST_ACTIONS[0]:
			user.set_room_temp('question', 'trade')

			reply(get_message(user, 'trade_items'))
		elif text == FIRST_ACTIONS[1]:
			user.set_room_temp('question', 'order')	
			reply(get_message(user, 'new_order_list'))
		elif text == FIRST_ACTIONS[2]:
			reply(
				'Ты избил всех дварфов (Благо они маленькие и ты просто пинал их по лицу) и '
				'забрал все вещи и деньги! Так держать, Воришка!'
			)
			steal(user)
			leave(user, reply, with_army=True)
		else:
			reply('Приятных путешествий! Мы еще встретимся.')
			leave(user, reply)
	elif question == 'order':
		if text == 'Назад':
			question = user.set_room_temp('question', 'first')
		elif order(user, text):
			reply('Попробуем что-то сделать.')
		else:
			reply('Будут накладки.')
	else:
		if text == 'Назад':
			question = user.set_room_temp('question', 'first')
		elif not buy(user, reply, text):
			reply('Таких вещей не привозили.')

		reply('Что-то еще?')
