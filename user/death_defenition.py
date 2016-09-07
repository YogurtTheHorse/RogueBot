import rooms.roomloader as roomloader

import logging
from constants import *

from localizations import locale_manager
import databasemanager as dbmanager

def update_leaderbord(self, reason=None):
	rate = 0
	if self.rooms_count > 0:
		try:
			rate = ((((self.get_damage() * self.get_mana_damage() + self.gold) / self.rooms_count) ** 0.5) ** 1.5) // 100 
		except:
			pass

	self.death_reason = reason
	dbmanager.add_to_leaderboard(self, rate, dbmanager.RATE_TABLE)
	dbmanager.add_to_leaderboard(self, self.rooms_count, dbmanager.ROOMS_TABLE)
	dbmanager.add_to_leaderboard(self, self.monsters_killed, dbmanager.KILLS_TABLE)

def death(self, reply, reason=None):
	if self.state == 'room':
		room = roomloader.load_room(self.room[1], self.room[0])
		reply(locale_manager.get('DEATH_PLACE').format(room.name))

	self.dead = True
	self.state = ''

	self.update_leaderbord(reason)

	reply(locale_manager.get('DEAD_MESSAGE').format(self.monsters_killed, self.rooms_count), [ '/start' ])

	if 'save' in self.variables:
		self.recover(reply)

def reborn(self, reply, answer, name=None):
	self.state = 'reborned'
	self.reborn_answer = answer
	reason = 'Перерождение'
	if name is not None:
		reason += ' ({0})'.format(name)

	self.update_leaderbord(reason=reason)

	if 'save' in self.variables:
		self.recover(reply)
	
