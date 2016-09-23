import logging
from constants import *

from localizations import locale_manager

def open_corridor(self, reply):
	if self.state == 'room':
		for item in self.get_items():
			item.on_corridor(self, reply)

	self.state = 'corridor'
	reply(self.get_stats())

	buttons = [ 
		locale_manager.get('OPEN_NEXT_DOOR'), 
		locale_manager.get('PLAYER_CHARACTERISTICS')#, locale_manager.get('JOIN_TORNAMENT')
	]

	if self.has_item('sign'):
		buttons.append(locale_manager.get('USE_SIGN'))

	if not self.prayed:
		buttons.append(locale_manager.get('PRAY_TO_GOD'))

	if not self.visited_shop:
		buttons.append(locale_manager.get('OPEN_SHOP'))

	if self.race == RAT_RACE:
		buttons.append('Умереть')			

	if len(self.items) > 0:
		buttons.append(locale_manager.get('SHOW_INVENTORY'))

	reply(locale_manager.get('WHAT_WILL_WE_DO'), buttons)

def corridor(self, reply, text):
	if self.has_tag('wet'):
		self.remove_tag('wet')
	if self.has_tag('wet_enemy'):
		self.remove_tag('wet_enemy')

	if text.startswith(locale_manager.get('OPEN_NEXT_DOOR').split()[0]):
		self.open_room(reply)
	elif text == locale_manager.get('USE_SIGN'):
		self.open_room(reply, 'special', 'sign')
	elif text.startswith(locale_manager.get('PRAY_TO_GOD').split()[0]):
		self.pray(reply)
	elif text.startswith(locale_manager.get('OPEN_SHOP').split()[0]):
		self.open_shop(reply)
	elif text.startswith(locale_manager.get('SHOW_INVENTORY').split()[0]):
		self.inventory_page = 0
		self.open_inventory(reply)
	elif text.startswith(locale_manager.get('PLAYER_CHARACTERISTICS').split()[0]):
		self.show_characteristics(reply)
	elif text == 'Умереть':
		self.death(reply, reason='Суицид')
	elif text == locale_manager.get('JOIN_TORNAMENT'):
		self.open_room(reply, 'usual', 'cesar')
	else:
		self.open_corridor(reply)
