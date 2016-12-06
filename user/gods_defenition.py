import random
from datetime import datetime
from utils.buffs import EmperorBurn
from utils.buffs import EmperorDefence

import logging
from constants import *

from localizations import locale_manager

def evilgod(self, reply, god):
	self.gods_level = [ 0 for g in self.gods ]

	if god == locale_manager.get('buddha'): # Buddha
		txt = ()
		reply(locale_manager.get('gods.evil_buddha'))
	elif god == locale_manager.get('jesus'): # Jesus
		txt = ()
		self.make_damage(5, 10, reply, death=False)
		reply(locale_manager.get('gods.evil_jesus'))
	elif god == locale_manager.get('allah'): # Allah
		self.make_damage(20, 30, reply, name='death_reason.allah')
		reply(locale_manager.get('gods.evil_allah'))
	elif god == locale_manager.get('author'): # Author
		self.add_item('special', 'intoxicated_shoes')
		reply(locale_manager.get('gods.evil_author'))
	elif god == locale_manager.get('emperor'): # Emperor
		self.new_buff(EmperorBurn())
		reply(locale_manager.get('gods.evil_emperor'))	

def god_love(self, reply, god):
	if god == BUDDHA_NUM: # Buddha
		reply(locale_manager.get('gods.buddha_love'))
		self.mp = self.max_mp
	elif god == JESUS_NUM: # Jesus
		reply(locale_manager.get('gods.jesus_love'))
		self.add_item('special', 'wine')
	elif god == ALLAH_NUM: # Allah
		reply(locale_manager.get('gods.allah_love'))
		self.hp = self.max_hp
	elif god == AUTHOR_NUM: # Author
		reply(locale_manager.get('gods.author_love'))
		self.open_room(reply, 'special', 'icecream')
	elif god == EMPEROR_NUM: # Emperor
		reply(locale_manager.get('gods.emperor_love'))
		self.new_buff(EmperorDefence())	

def prayto(self, reply, god):
	god_num = -1

	if god == self.gods[BUDDHA_NUM]: # Buddha
		reply(locale_manager.get('gods.buddha_prayed'))
		god_num = BUDDHA_NUM
	elif god == self.gods[JESUS_NUM]: # Jesus
		reply(locale_manager.get('gods.jesus_prayed'))
		god_num = JESUS_NUM
	elif god == self.gods[ALLAH_NUM]: # Allah
		reply(locale_manager.get('gods.allah_prayed'))
		god_num = ALLAH_NUM
	elif god == self.gods[AUTHOR_NUM]: # Author
		reply(locale_manager.get('gods.author_prayed'))
		god_num = AUTHOR_NUM
	elif god == self.gods[EMPEROR_NUM]: # Emperor
		reply(locale_manager.get('gods.emperor_prayed'))
		god_num = EMPEROR_NUM	
	else:
		reply(locale_manager.get('gods.no_god'))

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
			reply(locale_manager.get('gods.fast_god'))
		else:
			reply(locale_manager.get('gods.god_ask'), [ locale_manager.get(g) for g in self.gods] )
	elif god not in self.gods:
		reply(locale_manager.get('gods.no_god'), self.gods)
	else:
		if len(self.last_god) > 0 and god != self.last_god:
			self.evilgod(reply, self.last_god)

		self.prayto(reply, god)
		self.last_god = god

def divine_intervention(self, reply):
	res = random.random()

	# 2 hours or dead ?
	if (datetime.now() - self.last_message).total_seconds() > 60 * 60 * 2 or self.dead:
		return

	if self.has_item('intoxicated_shoes'):
		reply(locale_manager.get('divine.divine_forgives'))
		self.remove_item('intoxicated_shoes')
	else:
		if res < 0.1 and not self.has_item('assasin_ticket'):
			self.add_item('special', 'assasin_ticket')
			reply(locale_manager.get('divine.divine_assasin'))
		elif res < 0.55 and self.hp < self.max_hp:
			self.heal(self.max_hp // 2)
			reply(locale_manager.get('divine.divine_heal'))
		elif self.mp < self.max_mp:
			self.mana(self.max_mp // 2)
			reply(locale_manager.get('divine.divine_mana'))
		else:
			self.give_gold(2000)
