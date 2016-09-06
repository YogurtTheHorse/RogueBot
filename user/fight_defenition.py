import items.itemloader as itemloader
import rooms.roomloader as roomloader

import logging
from constants import *

from localizations import locale_manager

def get_fight_actions(self):
	actions = [
		locale_manager.get('KICK_ARM'),
		locale_manager.get('KICK_MAGIC'),
		locale_manager.get('USE') + locale_manager.get('IMAGINATION')
	]

	for i in self.get_items():
		if i.fightable:
			act = locale_manager.get('USE') + i.name
			if act not in actions:
				actions.append(act)

	return actions

def fight_dice(self, reply, result, subject=None):
	room = roomloader.load_room(self.room[1], self.room[0])
	if subject == 'noname':
		dmg = result + self.get_damage_bonus(reply) // 2

		reply(locale_manager.get('IMAGINATION_FIGHT').format(dmg))

		room.make_damage(self, reply, dmg)
		
		if self.state == 'room':
			self.fight_answer(reply)
			reply(self.get_stats())


def fight_action(self, reply, text):
	room = roomloader.load_room(self.room[1], self.room[0])
	if text == locale_manager.get('KICK_ARM'):
		dmg = self.get_damage() + self.get_damage_bonus(reply)

		reply(locale_manager.get('MONSTER_DAMAGED').format(dmg))

		room.make_damage(self, reply, dmg)
	elif text == locale_manager.get('KICK_MAGIC'):
		dmg = self.get_mana_damage()

		reply(locale_manager.get('MAGIC_KICKED').format(dmg))

		room.make_damage(self, reply, dmg)
	elif text.startswith(locale_manager.get('USE')):
		name = text[len(locale_manager.get('USE')):]
		item = None

		for i in self.get_items():
			if i.name == name:
				item = i
				break

		if item:
			dmg = item.fight_use(self, reply, room)
			if dmg != 0:
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
	room = roomloader.load_room(self.room[1], self.room[0])
	if room.code_name == 'tornament':
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

def won(self, reply, tornament=False):
	room = roomloader.load_room(self.room[1], self.room[0])

	if room.code_name == 'tornament' and tornament:
		reply('Стоп. Это же турнир, тут все работает не так. Ты просто нанес огромный урон противникам. Примерно `100`')
		room.make_damage(self, reply, 100)
		return

	self.monsters_killed += 1

	items = [ itemloader.load_item(i, 'loot') for i in room.loot ]
	loot = ', '.join([ item.name for item in items ]) if len(items) > 0 else 'Ничего.'

	for lt in room.loot:
		self.add_item('loot', lt)

	if room.coins > 0:
		reply(locale_manager.get('GOLD_FOUND').format(room.coins))

		self.gold += room.coins

	reply(locale_manager.get('YOU_WON').format(loot))

	self.leave(reply)