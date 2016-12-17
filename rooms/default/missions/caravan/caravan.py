from localizations import locale_manager
import random
from items import itemloader

name = locale_manager.get('rooms.default.missions_caravan.caravan.phrase_103')

FIRST_ACTIONS = [ locale_manager.get('rooms.default.missions_caravan.caravan.phrase_104'), locale_manager.get('rooms.default.missions_caravan.caravan.phrase_105'), locale_manager.get('rooms.default.missions_caravan.caravan.phrase_106'), locale_manager.get('rooms.default.missions_caravan.caravan.phrase_107') ]

def enter(user, reply):
	reply(
		locale_manager.get('rooms.default.missions_caravan.caravan.phrase_101'),
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

	user.set_room_temp(lst + locale_manager.get('rooms.default.missions_caravan.caravan.phrase_108'), names)
	user.set_room_temp(lst + locale_manager.get('rooms.default.missions_caravan.caravan.phrase_109'), descriptions)
	user.set_room_temp(lst + locale_manager.get('rooms.default.missions_caravan.caravan.phrase_110'), costs)

def get_actions(user):
	question = user.get_room_temp('question', def_val='first')
	
	if question == 'first':
		return FIRST_ACTIONS
	elif question == 'trade':
		return user.get_room_temp('trade_items_names') + [ locale_manager.get('rooms.default.missions_caravan.caravan.phrase_111') ]
	elif question == 'order':
		return user.get_room_temp('new_order_list_names') + [ locale_manager.get('rooms.default.missions_caravan.caravan.phrase_112') ]

def get_message(user, lst):
	names = user.get_room_temp(lst + locale_manager.get('rooms.default.missions_caravan.caravan.phrase_113'), [])
	descriptions = user.get_room_temp(lst + locale_manager.get('rooms.default.missions_caravan.caravan.phrase_114'), [])
	costs = user.get_room_temp(lst + locale_manager.get('rooms.default.missions_caravan.caravan.phrase_115'), [])

	msg = locale_manager.get('rooms.default.missions_caravan.caravan.phrase_116')
	msg += locale_manager.get('rooms.default.missions_caravan.caravan.phrase_117').join([ locale_manager.get('rooms.default.missions_caravan.caravan.phrase_118').format(name, costs[i], descriptions[i]) for i, name in enumerate(names) ])

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

			reply(locale_manager.get('rooms.default.missions_caravan.caravan.phrase_119').format(name, costs[ind]))
		else:
			reply(locale_manager.get('rooms.default.missions_caravan.caravan.phrase_120'))


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
				locale_manager.get('rooms.default.missions_caravan.caravan.phrase_102'))
			steal(user)
			leave(user, reply, with_army=True)
		else:
			reply(locale_manager.get('rooms.default.missions_caravan.caravan.phrase_121'))
			leave(user, reply)
	elif question == 'order':
		if text == locale_manager.get('rooms.default.missions_caravan.caravan.phrase_122'):
			question = user.set_room_temp('question', 'first')
		elif order(user, text):
			reply(locale_manager.get('rooms.default.missions_caravan.caravan.phrase_123'))
		else:
			reply(locale_manager.get('rooms.default.missions_caravan.caravan.phrase_124'))
	else:
		if text == locale_manager.get('rooms.default.missions_caravan.caravan.phrase_125'):
			question = user.set_room_temp('question', 'first')
		elif not buy(user, reply, text):
			reply(locale_manager.get('rooms.default.missions_caravan.caravan.phrase_126'))

		reply(locale_manager.get('rooms.default.missions_caravan.caravan.phrase_127'))
