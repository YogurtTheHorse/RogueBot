import rooms.roomloader as roomloader

import logging
import statistics
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
		room = roomloader.load_room(self.room[1], self.room[0], self)
		room.on_death(self, reply)
		reply(locale_manager.get('DEATH_PLACE').format(room.name))

	self.dead = True
	self.state = ''

	self.update_leaderbord(reason)
	track_stats = {
		'uid': self.uid, 
		'reason': reason, 
		'rooms_count': self.rooms_count,
		'gold': self.gold,
		'kills_count': self.monsters_killed,
		'damage': self.get_damage(),
		'defence': self.get_defence(),
		'charisma': self.get_charisma(),
		'mana_damage': self.get_mana_damage(),
		'live_time': self.get_live_time()
	}
	statistics.track(self.uid, track_stats, 'Death')

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
	
