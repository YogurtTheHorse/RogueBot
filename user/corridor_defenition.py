import logging
import rooms.roomloader as roomloader

from constants import *

from localizations import locale_manager

def open_corridor(self, reply):
	if self.state == 'room':
		for item in self.get_items():
			item.on_corridor(self, reply)

	self.state = 'corridor'
	reply(self.get_stats())

	buttons = [ 
		locale_manager.get('corridor.open_next_door'), 
		locale_manager.get('corridor.player_characteristics')#, locale_manager.get('JOIN_TORNAMENT')
	]

#	if not self.get_variable('halloween_visited', False) and self.rooms_pack == 'default':
#		buttons.append('Хеллуин!')

	if self.has_item('sign'):
		buttons.append(locale_manager.get('corridor.use_sign'))

	levels_acts = [ ]
	if self.get_next_level() is not None:
		levels_acts.append(locale_manager.get('corridor.go_down'))

	if self.get_prev_level() is not None:
		levels_acts.append(locale_manager.get('corridor.go_up'))

	if len(levels_acts) > 0:
		buttons.append(levels_acts)

	if not self.prayed:
		buttons.append(locale_manager.get('corridor.pray_ro_god'))

	if not self.visited_shop:
		buttons.append(locale_manager.get('corridor.open_shop'))

	if self.race == RAT_RACE:
		buttons.append(locale_manager.get('corridor.die'))

	if len(self.items) > 0:
		buttons.append(locale_manager.get('corridor.show_inventory'))

	buttons.append(locale_manager.get('corridor.other'))

	reply(locale_manager.get('corridor.what_will_we_do'), buttons)

def corridor(self, reply, text):
	if self.has_tag('wet'):
		self.remove_tag('wet')
	if self.has_tag('wet_enemy'):
		self.remove_tag('wet_enemy')

	if text.startswith(locale_manager.get('corridor.open_next_door').split()[0]):
		self.open_room(reply)
	elif text == locale_manager.get('corridor.use_sign'):
		self.open_room(reply, 'special', 'sign')
	elif text.startswith(locale_manager.get('corridor.pray_to_god').split()[0]):
		self.pray(reply)
	elif text.startswith(locale_manager.get('corridor.open_shop').split()[0]):
		self.open_shop(reply)
	elif text.startswith(locale_manager.get('corridor.show_inventory').split()[0]):
		self.inventory_page = 0
		self.open_inventory(reply)
	elif text.startswith(locale_manager.get('corridor.show_inventory').split()[0]):
		self.show_characteristics(reply)
#	elif text == 'Хеллуин!' and not self.get_variable('halloween_visited', False):
#		self.open_room(reply, 'special', 'helloween_shop')
#		self.set_variable('halloween_visited', True)
	elif text == locale_manager.get('corridor.die'):
		reply(locale_manager.get('corridor.died'), photo='BQADAgAD5wgAAmrZzgcHFvPa24KvDwI')
		self.death(reply, reason='Суицид')
	elif text == locale_manager.get('corridor.join_tornament'):
		self.open_room(reply, 'usual', 'cesar')
	elif self.get_prev_level() is not None and text == locale_manager.get('corridor.go_up'):
		self.level = self.get_prev_level()
		reply(locale_manager.get('corridor.died'))

		msg = ''
		for ind, name in enumerate(roomloader.get_level_rooms(self, self.level)):
			msg += '{0}. {1}\n'.format(ind + 1, name)

		reply(msg)

		self.open_corridor(reply)
	elif self.get_next_level() is not None and text == locale_manager.get('corridor.go_down'):
		self.level = self.get_next_level()
		reply(locale_manager.get('corridor.went_down'))

		msg = ''
		for ind, name in enumerate(roomloader.get_level_rooms(self, self.level)):
			msg += '{0}. {1}\n'.format(ind + 1, name)

		reply(msg)

		self.open_corridor(reply)
	elif text == locale_manager.get('corridor.other'):
		self.open_other(reply)
	else:
		self.open_corridor(reply)
