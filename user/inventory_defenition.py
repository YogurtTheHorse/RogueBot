import logging
from constants import *

from collections import Counter
from localizations import locale_manager

def open_inventory(self, reply):
	self.state = 'inventory'

	items = self.get_items()
	active_items = self.get_active_items()

	if len(items) == 0:
		self.open_corridor(reply)
		return

	actions = [ ]
	msg = locale_manager.get('INVENTORY_MESSAGE')

	counter_items = Counter(items)
	selected_items = list(counter_items)

	begin = min(self.inventory_page * INVENTORY_PAGE_SIZE, len(selected_items) - 1)
	end = min((self.inventory_page + 1) * INVENTORY_PAGE_SIZE, len(selected_items))

	for i in selected_items[begin:end]:
		if i is not None:
			acts = [ ]
			is_atcive = ''#'(Надето: {0} шт.)'.format(active_items.count(i)) if i in active_items else ''
			msg += '{0} ({2} шт. ценой {4} злт.) {1}:\n{3}\n\n'.format(i.name, is_atcive, counter_items[i], i.description, round(i.price * 0.7))
			if i.usable:
				acts.append(i.name)

			if active_items.count(i) > 0:
				pass#actions.append(locale_manager.get('DEACTIVATE') + i.name)

			if active_items.count(i) < items.count(i) and (len(active_items) < self.get_active_slots_len()):
				pass#actions.append(locale_manager.get('ACTIVATE') + i.name)

			acts.append(locale_manager.get('THROW_AWAY') + i.name)
			acts.append(locale_manager.get('SELL') + i.name)

			actions.append(acts)

	if begin > 0:
		actions.append(locale_manager.get('BACK'))
	if end < len(selected_items):
		actions.append(locale_manager.get('NEXT'))

	actions.append(locale_manager.get('TO_CORRIDOR'))
	reply(msg, actions)

def inventory(self, reply, text):
	if text == locale_manager.get('TO_CORRIDOR'):
		self.open_corridor(reply)
	elif False and text.startswith(locale_manager.get('ACTIVATE')):
		name = text[len(locale_manager.get('ACTIVATE')):]

		item = self.get_item_by_name(name)

		items = self.get_items()
		active_items = self.get_active_items()
		
		if item is not None and active_items.count(item) < items.count(item) and (len(active_items) < self.get_active_slots_len()):
			self.active_items.append((item.buff, item.code_name))
			reply(locale_manager.get('ACTIVATED'))
		else:
			reply(locale_manager.get('CANT_ACTIVATE'))

		self.open_inventory(reply)
	elif False and text.startswith(locale_manager.get('DEACTIVATE')):
		name = text[len(locale_manager.get('DEACTIVATE')):]

		item = self.get_item_by_name(name)

		self.deactivate_item_by_name(name)
		self.open_inventory(reply)
	elif text.startswith(locale_manager.get('THROW_AWAY')):
		name = text[len(locale_manager.get('THROW_AWAY')):]

		if not self.remove_item_by_name(name):
			reply(locale_manager.get('CANT_THROW'))

		self.open_inventory(reply)
	elif text.startswith(locale_manager.get('SELL')):
		name = text[len(locale_manager.get('SELL')):]

		item = self.get_item_by_name(name)
		if not self.remove_item_by_name(name):
			reply('Не продается')
			self.open_inventory(reply)
		else:
			reply('Золотишко-то.. Звенит!')
			self.give_gold(round(item.price * 0.7))
			self.open_inventory(reply)
	elif text == locale_manager.get('BACK'):
		self.inventory_page = max(self.inventory_page - 1, 0)
		self.open_inventory(reply)
	elif text == locale_manager.get('NEXT'):
		self.inventory_page = self.inventory_page + 1
		self.open_inventory(reply)
	else:
		items = self.get_items()
		
		for i in items:
			if i.name == text:
				i.on_use(self, reply)

				if i.disposable:
					self.remove_item(i.code_name)

				break
		
		if self.state == 'inventory':
			self.open_corridor(reply)