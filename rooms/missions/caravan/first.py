from items import itemloader

name = 'Караван Дварфов'

FIRST_ACTIONS = [ 'Договориться', 'Уйти' ]

def enter(user, reply):
	reply(
		'Ты открываешь дверь и видишь целый караван дварфов!\n'
		'К тебе подходит рыжебородый дварф в доспехах и начинает разговор:\n\n'
		'— Привет, Путник! Мы путешествуем по этим комнатам и предоставляем '
		'услуги торговли. Можешь заказать чего-нибудь и мы доставим тебе!'
	)

	user.set_room_temp('question', 'first')

	generate_trade_items(user)
	generate_items_text(user)

def generate_trade_items(user):
	items = [ ]

	for i in range(7):
		item = itemloader.load_random_item('good')

		while item in items:
			item = itemloader.load_random_item('good')

		items.append(item)

	user.set_room_temp('trade_items', items)

def generate_items_text(user):
	trade_items = user.get_room_temp('trade_items', def_val=[ ])

	items =  [ itemloader.load_item(i[1], i[0]) for i in trade_items ]

	names = [ i.name for i in items ]
	descriptions = [ i.description for i in items if i is not None ]
	costs = [ i.price * 2 for i in items if i is not None ]

	user.set_room_temp('names', names)
	user.set_room_temp('descriptions', descriptions)
	user.set_room_temp('costs', costs)

def get_actions(user):
	question = user.get_room_temp('question', def_val='first')
	
	if question == 'first':
		return FIRST_ACTIONS
	elif question == 'trade':
		return user.get_room_temp('names') + [ 'Выйти' ]

def get_message(user):
	names = user.get_room_temp('names', [])
	descriptions = user.get_room_temp('descriptions', [])
	costs = user.get_room_temp('costs', [])

	msg = 'Выбирай, что привезти с собой (Оплата после доставки):\n\n'
	msg += '\n\n'.join([ '{0}\nЦена (Доставка + покупка): {1}\n{2}'.format(name, costs[i], descriptions[i]) for i, name in enumerate(names) ])

	return msg

def order(user, name):
	names = user.get_room_temp('names', [])
	descriptions = user.get_room_temp('descriptions', [])
	costs = user.get_room_temp('costs', [])

	if name in names:
		trade_items = user.get_room_temp('trade_items', def_val=[ ])
		ind = names.index(name)

		item = trade_items[ind]

		del trade_items[ind]
		del names[ind]
		del descriptions[ind]
		del costs[ind]

		user.set_room_temp('trade_items', trade_items)
		user.set_room_temp('names', names)
		user.set_room_temp('descriptions', descriptions)
		user.set_room_temp('costs', costs)

		order_list = user.get_variable('order_list', def_val=[ ])
		order_list.append(item)
		user.set_variable('order_list', order_list)

		return True
	else:
		return False

def leave(user, reply):
	user.leave(reply)
	user.new_mission('caravan', 'caravan', path_len=1)

def action(user, reply, text):
	question = user.get_room_temp('question', def_val='first')

	if question == 'first':
		if text == FIRST_ACTIONS[0]:
			user.set_room_temp('question', 'trade')

			reply(get_message(user))
		else:
			reply('Приятных путешествий! Мы еще встретимся.')
			leave(user, reply)
	else:
		if text == 'Выйти' or len(user.get_room_temp('names')) == 0:
			reply('До новых встреч! Мы еще вернемся.')
			leave(user, reply)
		elif order(user, text):
			reply('Постараемся привезти в кратчайшие сроки.')
		else:
			reply('Могут возникнуть проблемы с доставкой.')


		reply('Что-то еще?')
