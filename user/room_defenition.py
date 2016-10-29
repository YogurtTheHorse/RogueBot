import random
import statistics

import rooms.roomloader as roomloader

from constants import *

from localizations import locale_manager

import logging
logger = logging.getLogger('rg')

def make_damage(self, mn, mx, reply, death=True, defence=True, name=None):
	old_hp = self.hp

	dmg = random.randint(mn, mx)
	if defence:
		defe = self.get_defence()

		# Пока не удаляю, так как надо подумать как это поменять
		# dmg = max(dmg + self.rooms_count // 20 - defe, 1)
		dmg *= 1 - (defe / ( 70 + defe))

	self.hp -= round(dmg)

	if not death:
		self.hp = max(self.hp, 1)
	elif self.hp <= 0:
		if name is None and self.state == 'room':
			room = roomloader.load_room(self.room[1], self.room[0], self)
			name = room.name

		self.death(reply, reason=name)

	return old_hp - self.hp

def set_room_temp(self, name, val=None):
	self.room_temp[name] = val

def get_room_temp(self, name, def_val=None):
	if name in self.room_temp:
		return self.room_temp[name]
	else:
		return def_val

def open_room(self, reply, room_type=None, room_name=None):
	if room_name != 'halloween_shop':
		self.set_variable('halloween_visited', False)

	if self.race == RAT_RACE:
		reply('Ты — крыса, у тебя не хватило сил сдвинуть дверь с места :(')
		self.open_corridor(reply)
		return

	self.state = 'room'

	self.rooms_count += 1
	for m in self.missions:
		m.room_opened()

	if not (room_type and room_name):
		room_type, room_name = roomloader.get_next_room(self)

	logger.info('room_opened ' + room_name)

	last_mission = self.get_last_mission()
	if last_mission.get_room_type() == room_type and last_mission.get_room_name() == room_name:
		self.pop_mission()

	self.room = (room_type, room_name)
	self.room_temp = { }

	visited = self.get_perma_variable('visited_rooms', def_val=[])
	if room_name not in visited:
		visited.append(room_name)
	self.set_perma_variable('visited_rooms', visited)
	statistics.track(self.uid, {'uid': self.uid, 'name': room_name, 'type': room_type}, 'Room opened')

	room = roomloader.load_room(self.room[1], self.room[0], self)

	for i in self.get_items():
		i.on_room(self, reply, room)

	to_delete = [ ]
	for i, b in enumerate(self.buffs):
		try:
			b.on_room(self, reply, room)
			if b.time <= 0:
				to_delete.append(i)
		except:
			pass

	for i in reversed(to_delete):
		self.buffs[i].on_end(self, reply, room)
		del self.buffs[i]

	if self.pet:
		self.get_pet().on_room(self, reply, room)

	if room.room_type == 'monster':
		self.set_room_temp('hp', room.hp)

	reply(locale_manager.get('ROOM_OPENED'))
	reply(room.name + '!')

	room.enter(self, reply)

	if self.state == 'room':
		reply(locale_manager.get('YOUR_ACTIONS'), room.get_actions(self))

	if not room.can_open(self, reply):
		room.open_failure(self, reply)

		self.open_corridor(reply)
		return

def in_room(self, reply, text):
	room = roomloader.load_room(self.room[1], self.room[0], self)
	room.action(self, reply, text)

	if self.state == 'room':
		reply(self.get_stats())
		room = roomloader.load_room(self.room[1], self.room[0], self)
		reply(locale_manager.get('YOUR_ACTIONS'), room.get_actions(self))

def throw_dice(self, reply, subject=None):
	self.state = 'dice'
	self.subject = subject

	reply(locale_manager.get('DICE_TIME'), [locale_manager.get('THOW_DICE')])

def get_dice_bonus(self, reply):
	res = 0

	for i in self.get_items():
		res += i.get_dice_bonus(self, reply)

	if self.pet:
		res += self.get_pet().get_dice_bonus(self, reply)

	return res


def dice(self, reply, text):
	if text == locale_manager.get('THOW_DICE'):
		self.state = 'room'

		res = sum(random.randint(1, 8) for n in range(0, DICE_MAX // 8))
		res += self.get_dice_bonus(reply)
		reply(locale_manager.get('DICE_RESULT').format(res))
		
		room = roomloader.load_room(self.room[1], self.room[0], self)
		room.dice(self, reply, res, self.subject)

		if self.state == 'room':
			reply(locale_manager.get('YOUR_ACTIONS'), room.get_actions(self))
	else:
		reply(locale_manager.get('DICE_CONFIDENCE'), [locale_manager.get('THOW_DICE')])

def leave(self, reply):
	self.visited_shop = False
	self.shop_items = [ ]
	self.prayed = False

	room = roomloader.load_room(self.room[1], self.room[0], self)
	if room is not None:
		room.on_leave(self, reply)

	if self.hp < self.max_hp / 2:
		#reply('Ты слегка отдохнул')
		#self.hp = self.max_hp / 2
		pass

	self.open_corridor(reply)

def start_tornament(self, tid, reply):
	self.tornament_id = tid
	self.open_room(reply, 'special', 'tornament')
