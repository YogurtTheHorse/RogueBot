import random
from datetime import datetime
from utils.buffs import EmperorBurn
from utils.buffs import EmperorDefence

import logging
from constants import *

from localizations import locale_manager

def evilgod(self, reply, god):
	self.gods_level = [ 0 for g in self.gods ]

	if god == locale_manager.get('gods.buddha', self.lang): # Buddha
		txt = ()
		reply(locale_manager.get('gods.evil_buddha', self.lang))
	elif god == locale_manager.get('jesus', self.lang): # Jesus
		txt = ()
		self.make_damage(5, 10, reply, death=False)
		reply(locale_manager.get('gods.evil_jesus', self.lang))
	elif god == locale_manager.get('allah', self.lang): # Allah
		self.make_damage(20, 30, reply, name='death_reason.allah')
		reply(locale_manager.get('gods.evil_allah', self.lang))
	elif god == locale_manager.get('author', self.lang): # Author
		self.add_item('special', 'intoxicated_shoes')
		reply(locale_manager.get('gods.evil_author', self.lang))
	elif god == locale_manager.get('emperor', self.lang): # Emperor
		self.new_buff(EmperorBurn())
		reply(locale_manager.get('gods.evil_emperor', self.lang))	

def god_love(self, reply, god):
	if god == BUDDHA_NUM: # Buddha
		reply(locale_manager.get('gods.buddha_love', self.lang))
		self.mp = self.max_mp
	elif god == JESUS_NUM: # Jesus
		reply(locale_manager.get('gods.jesus_love', self.lang))
		self.add_item('special', 'wine')
	elif god == ALLAH_NUM: # Allah
		reply(locale_manager.get('gods.allah_love', self.lang))
		self.hp = self.max_hp
	elif god == AUTHOR_NUM: # Author
		reply(locale_manager.get('gods.author_love', self.lang))
		self.open_room(reply, 'special', 'icecream')
	elif god == EMPEROR_NUM: # Emperor
		reply(locale_manager.get('gods.emperor_love', self.lang))
		self.new_buff(EmperorDefence())	

def prayto(self, reply, god):
	god_num = -1

	if god == self.gods[BUDDHA_NUM]: # Buddha
		reply(locale_manager.get('gods.buddha_prayed', self.lang))
		god_num = BUDDHA_NUM
	elif god == self.gods[JESUS_NUM]: # Jesus
		reply(locale_manager.get('gods.jesus_prayed', self.lang))
		god_num = JESUS_NUM
	elif god == self.gods[ALLAH_NUM]: # Allah
		reply(locale_manager.get('gods.allah_prayed', self.lang))
		god_num = ALLAH_NUM
	elif god == self.gods[AUTHOR_NUM]: # Author
		reply(locale_manager.get('gods.author_prayed', self.lang))
		god_num = AUTHOR_NUM
	elif god == self.gods[EMPEROR_NUM]: # Emperor
		reply(locale_manager.get('gods.emperor_prayed', self.lang))
		god_num = EMPEROR_NUM	
	else:
		reply(locale_manager.get('gods.no_god', self.lang))

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
			reply(locale_manager.get('gods.fast_god', self.lang))
		else:
			reply(locale_manager.get('gods.god_ask', self.lang), [ locale_manager.get('gods.' + g) for g in self.gods] )
	elif god not in self.gods:
		reply(locale_manager.get('gods.no_god', self.lang), self.gods)
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
		reply(locale_manager.get('divine_intervantion.divine_forgives', self.lang))
		self.remove_item('intoxicated_shoes')
	else:
		if res < 0.1 and not self.has_item('assasin_ticket'):
			self.add_item('special', 'assasin_ticket')
			reply(locale_manager.get('divine_intervantion.divine_assasin', self.lang))
		elif res < 0.55 and self.hp < self.max_hp:
			self.heal(self.max_hp // 2)
			reply(locale_manager.get('divine_intervantion.divine_heal', self.lang))
		elif self.mp < self.max_mp:
			self.mana(self.max_mp // 2)
			reply(locale_manager.get('divine_intervantion.divine_mana', self.lang))
		else:
			self.give_gold(2000)
