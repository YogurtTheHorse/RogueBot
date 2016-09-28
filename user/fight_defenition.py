import items.itemloader as itemloader
import rooms.roomloader as roomloader
import bossmanager

import logging
from constants import *

from collections import Counter
from localizations import locale_manager

def get_fight_actions(self):
	actions = [
		locale_manager.get('KICK_ARM'),
		locale_manager.get('KICK_MAGIC'),
		locale_manager.get('USE') + locale_manager.get('IMAGINATION')
	]

	items = self.get_items()
	counter_items = Counter(items)
	for i, cnt in counter_items.most_common():
		if i.fightable:
			act = locale_manager.get('USE') + i.name + ' ({0} шт.)'.format(cnt)
			if act not in actions:
				actions.append(act)

	return actions

def fight_dice(self, reply, result, subject=None):
	room = roomloader.load_room(self.room[1], self.room[0], self)
	if subject == 'noname':
		dmg = result + self.get_damage_bonus(reply) // 2

		reply(locale_manager.get('IMAGINATION_FIGHT').format(dmg))

		room.make_damage(self, reply, dmg)
		
		if self.state == 'room':
			self.fight_answer(reply)
			reply(self.get_stats())


def fight_action(self, reply, text):
	room = roomloader.load_room(self.room[1], self.room[0], self)
	if text == locale_manager.get('KICK_ARM'):
		dmg = self.get_damage() + self.get_damage_bonus(reply)

		reply(locale_manager.get('MONSTER_DAMAGED').format(dmg))

		room.make_damage(self, reply, dmg)
	elif text == locale_manager.get('KICK_MAGIC'):
		dmg = self.get_mana_damage()

		if self.use_mana(5):
			reply(locale_manager.get('MAGIC_KICKED').format(dmg))

			room.make_damage(self, reply, dmg)
		else:
			reply('Маны то не хватает :(')
	elif text.startswith(locale_manager.get('USE')):
		name = 'foo'
		item = None

		if '(' in text:
			name = text[len(locale_manager.get('USE')):]
			name = name[:name.rindex('(')-1]

		for i in self.get_items():
			if i.name == name:
				item = i
				break

		if item:
			dmg = 0
			if item.can_use(self, reply, room):
				item.success(self, reply, room)
				dmg += item.fight_use(self, reply, room)
			else:
				item.failure(self, reply, room)

			if dmg != 0 and item.strengthoff is False:
				dmg += self.get_damage() + self.get_damage_bonus(reply)

			if item.disposable:
				self.remove_item(item.code_name)

			if self.state == 'room':
				reply(locale_manager.get('ITEM_USED').format(name, dmg))

				room.make_damage(self, reply, dmg)
		else:
			reply(locale_manager.get('NO_FIGHT_THING'))

			self.throw_dice(reply, 'noname')
	else:
		reply(locale_manager.get('DIDNT_UNDERSTAND'))

	if self.state == 'room':
		self.fight_answer(reply)

def fight_answer(self, reply):
	room = roomloader.load_room(self.room[1], self.room[0], self)
	if room.code_name == 'tornament':
		return

	room_type, room_name = self.room
	if room_type == 'boss':
		boss = bossmanager.current()
		user_boss_id = self.get_room_temp('boss_id', def_val=0)

		if boss.get('alive') is False or boss.get('id') is not user_boss_id:
			return

	a, b = room.damage_range
	dmg = self.make_damage(a, b, reply, name=room.name)

	if not self.dead and dmg > 0.2:
		reply(locale_manager.get('USER_DAMAGED').format(dmg))

def escape(self, reply, success=True):
	for i in self.get_items():
		i.on_escape(self, reply, success)

	if success:
		self.leave(reply)

def won(self, reply, tornament=False, boss=None):
	room = roomloader.load_room(self.room[1], self.room[0], self)

	if room.code_name == 'tornament' and tornament:
		reply('Стоп. Это же турнир, тут все работает не так. Ты просто нанес огромный урон противникам. Примерно `100`')
		room.make_damage(self, reply, 100)
		return

	self.monsters_killed += 1
	room.on_won(self, reply)

	items = [ itemloader.load_item(i, 'loot') for i in room.loot ]
	loot = ', '.join([ item.name for item in items ]) if len(items) > 0 else 'Ничего.'

	for lt in room.loot:
		self.add_item('loot', lt)

	if room.room_type == 'boss' and boss is not None:
		total_damage = self.get_room_temp('user_damage', def_val=0)

		if total_damage >= 1:
			room.coins = round(total_damage / boss['max_hp'] * boss['coins'])

		else:
			room.coins = 0

	if room.coins > 0:
		reply(locale_manager.get('GOLD_FOUND').format(room.coins))

		self.give_gold(room.coins)

	reply(locale_manager.get('YOU_WON').format(loot))

	if room.room_type != 'boss':
		self.leave(reply)