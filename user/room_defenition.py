import random

import rooms.roomloader as roomloader

import logging
from constants import *

from localizations import locale_manager

def make_damage(self, mn, mx, reply, death=True, defence=True, name=None):
	old_hp = self.hp

	dmg = random.randint(mn, mx)
	if defence:
		dmg = max(dmg + self.rooms_count // 20 - self.get_defence(), 1)
	self.hp -= dmg

	if not death:
		self.hp = max(self.hp, 1)
	elif self.hp <= 0:
		if name is None and self.state == 'room':
			room = roomloader.load_room(self.room[1], self.room[0])
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
	if self.race == RAT_RACE:
		reply('Ты крыса, у тебя не хватило сил сдвинуть дверь с места :(')
		self.open_corridor(reply)
		return

	self.state = 'room'

	self.rooms_count += 1

	if not (room_type and room_name):
		if self.rooms_to_story < 1:
			room_type, room_name = 'story', self.next_story_room
		else:
			self.rooms_to_story -= 1
			room_type, room_name = roomloader.get_next_room()

	self.room = (room_type, room_name)
	self.room_temp = { }

	room = roomloader.load_room(self.room[1], self.room[0])

	if room_type == 'story':
		self.story_level += 1
		self.next_story_room = room.next_story_room

		mn, mx = room.next_story_room_range
		self.rooms_to_story = random.randint(mn, mx)

	for i in self.get_items():
		i.on_room(self, reply, room)

	if room.room_type == 'monster':
		self.set_room_temp('hp', room.hp)

	reply(locale_manager.get('ROOM_OPENED'))
	reply(room.name + '!')

	room.enter(self, reply)

	if self.state == 'room':
		reply(locale_manager.get('YOUR_ACTIONS'), room.get_actions(self))

def in_room(self, reply, text):
	room = roomloader.load_room(self.room[1], self.room[0])
	room.action(self, reply, text)

	if self.state == 'room':
		reply(self.get_stats())
		room = roomloader.load_room(self.room[1], self.room[0])
		reply(locale_manager.get('YOUR_ACTIONS'), room.get_actions(self))

def throw_dice(self, reply, subject=None):
	self.state = 'dice'
	self.subject = subject

	reply(locale_manager.get('DICE_TIME'), [locale_manager.get('THOW_DICE')])

def get_dice_bonus(self, reply):
	res = 0

	for i in self.get_items():
		res += i.get_dice_bonus(self, reply)

	return res


def dice(self, reply, text):
	if text == locale_manager.get('THOW_DICE'):
		self.state = 'room'

		res = random.randint(1, DICE_MAX)
		res += self.get_dice_bonus(reply)
		reply(locale_manager.get('DICE_RESULT').format(res))
		
		room = roomloader.load_room(self.room[1], self.room[0])
		room.dice(self, reply, res, self.subject)

		if self.state == 'room':
			reply(locale_manager.get('YOUR_ACTIONS'), room.get_actions(self))
	else:
		reply(locale_manager.get('DICE_CONFIDENCE'), [locale_manager.get('THOW_DICE')])

def leave(self, reply):
	self.visited_shop = False
	self.prayed = False

	if self.hp < self.max_hp / 2:
		#reply('Ты слегка отдохнул')
		#self.hp = self.max_hp / 2
		pass

	self.open_corridor(reply)