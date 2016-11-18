import random
from datetime import datetime
from utils.buffs import EmperorBurn
from utils.buffs import EmperorDefence

import logging
from constants import *

from localizations import locale_manager

def evilgod(self, reply, god):
	self.gods_level = [ 0 for g in self.gods ]

	if god == self.gods[0]: # Buddha
		txt = ()
		reply(locale_manager.get('EVIL_BUDDHA'))
	elif god == self.gods[1]: # Jesus
		txt = ()
		self.make_damage(5, 10, reply, death=False)
		reply(locale_manager.get('EVIL_JESUS'))
	elif god == self.gods[2]: # Allah
		self.make_damage(20, 30, reply, name='Аллах')
		reply(locale_manager.get('EVIL_ALLAH'))
	elif god == self.gods[3]: # Author
		self.add_item('special', 'intoxicated_shoes')
		reply(locale_manager.get('EVIL_AUTHOR'))
	elif god == self.gods[4]: # Emperor
		self.new_buff(EmperorBurn())
		reply(locale_manager.get('EVIL_EMPEROR'))	

def god_love(self, reply, god):
	if god == BUDDHA_NUM: # Buddha
		reply(locale_manager.get('BUDDHA_LOVE'))
		self.mp = self.max_mp
	elif god == JESUS_NUM: # Jesus
		reply(locale_manager.get('JESUS_LOVE'))
		self.add_item('special', 'wine')
	elif god == ALLAH_NUM: # Allah
		reply(locale_manager.get('ALLAH_LOVE'))
		self.hp = self.max_hp
	elif god == AUTHOR_NUM: # Author
		reply(locale_manager.get('AUTHOR_LOVE'))
		self.open_room(reply, 'special', 'icecream')
	elif god == EMPEROR_NUM: # Emperor
		reply(locale_manager.get('EMPEROR_LOVE'))
		self.new_buff(EmperorDefence())	

def prayto(self, reply, god):
	god_num = -1

	if god == self.gods[BUDDHA_NUM]: # Buddha
		reply(locale_manager.get('BUDDHA_PRAYED'))
		god_num = BUDDHA_NUM
	elif god == self.gods[JESUS_NUM]: # Jesus
		reply(locale_manager.get('JESUS_PRAYED'))
		god_num = JESUS_NUM
	elif god == self.gods[ALLAH_NUM]: # Allah
		reply(locale_manager.get('ALLAH_PRAYED'))
		god_num = ALLAH_NUM
	elif god == self.gods[AUTHOR_NUM]: # Author
		reply(locale_manager.get('AUTHOR_PRAYED'))
		god_num = AUTHOR_NUM
	elif god == self.gods[EMPEROR_NUM]: # Emperor
		reply(locale_manager.get('EMPEROR_PRAYED'))
		god_num = EMPEROR_NUM	
	else:
		reply(locale_manager.get('NO_GOD'))

	if god_num >= 0:
		self.gods_level[god_num] += 1

		for item in self.get_items():
			item.on_pray(self, reply, god_num)


		if self.gods_level[god_num] >= GOD_LEVEL:
			self.god_love(reply, god_num)


	if self.state == 'pray':
		self.prayed = True
		self.open_corridor(reply)


def pray(self, reply, god=None):
	if self.prayed:
		return self.open_corridor(reply)

	self.state = 'pray'

	if god == None:
		if self.prayed:
			reply(locale_manager.get('FAST_GOD'))
		else:
			reply(locale_manager.get('GOD_ASK'), self.gods)
	elif god not in self.gods:
		reply(locale_manager.get('NO_GOD'), self.gods)
	else:
		if len(self.last_god) > 0 and god != self.last_god:
			self.evilgod(reply, self.last_god)

		self.prayto(reply, god)
		self.last_god = god

def divine_intervention(self, reply):
	res = random.random()

	try:
		if (datetime.now() - self.last_message).total_seconds() > 60 * 60 * 2:
			return
	except:
		self.last_message = datetime.now()

	if self.dead:
		return

	if self.has_item('intoxicated_shoes'):
		reply(locale_manager.get('DIVINE_FORGIVES'))
		self.remove_item('intoxicated_shoes')
	else:
		if res < 0.1 and not self.has_item('assasin_ticket'):
			self.add_item('special', 'assasin_ticket')
			reply(locale_manager.get('DIVINE_ASSASIN'))
		elif res < 0.55 and self.hp < self.max_hp:
			self.heal(self.max_hp // 2)
			reply(locale_manager.get('DIVINE_HEAL'))
		elif self.mp < self.max_mp:
			self.mana(self.max_mp // 2)
			reply(locale_manager.get('DIVINE_MANA'))
		else:
			self.give_gold(2000)
