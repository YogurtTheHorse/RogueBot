import random

from time import gmtime, strftime

import items.itemloader as itemloader
import rooms.roomloader as roomloader

import logging
from constants import *
from utils.names import names

from collections import Counter

from localizations.ru import *

logger = logging.getLogger('rg')

class User(object):
	def __init__(self, uid):
		super(User, self).__init__()

		self.uid = uid

		self.name = 'none'
		self.hp = 100
		self.mp = 100
		self.gold = 200

		self.max_hp = 150
		self.max_mp = 150

		self.state = 'name'

		self.items = [ ]
		self.inventory_page = 0

		self.gods = [ BUDDHA, JESUS, ALLAH, AUTHOR ]
		self.gods_level = [ 0 for g in self.gods ]
		self.last_god = ''
		self.prayed = False

		self.damage = 10
		self.defence = 1
		self.charisma = 0
		self.mana_damage = 0
		self.intelligence = 0

		self.visited_shop = False
		self.shop_items = [ ]
		self.shop_names = [ ]

		self.tags = [ ]

		self.room = ('', '')
		self.room_temp = { }

		self.reborn_answer = None
		self.dead = False

		self.rooms_to_story = random.randint(5, 25)
		self.next_story_room = 'first'
		self.story_level = 0

		self.subject = None

	def debug_info(self):
		msg = 'uid: ' + str(self.uid) + '\n'
		msg += 'name: ' + str(self.name) + '\n'
		msg += 'hp: ' + str(self.hp) + '\n'
		msg += 'mp: ' + str(self.mp) + '\n'
		msg += 'gold: ' + str(self.gold) + '\n'
		msg += 'max_hp: ' + str(self.max_hp) + '\n'
		msg += 'max_mp: ' + str(self.max_mp) + '\n'
		msg += 'state: ' + str(self.state) + '\n'
		msg += 'items: ' + str(self.items) + '\n'
		msg += 'inventory_page: ' + str(self.inventory_page) + '\n'
		msg += 'gods: ' + str(self.gods) + '\n'
		msg += 'gods_level: ' + str(self.gods_level) + '\n'
		msg += 'gods: ' + str(self.gods) + '\n'
		msg += 'last_god: ' + str(self.last_god) + '\n'
		msg += 'prayed: ' + str(self.prayed) + '\n'
		msg += 'damage: ' + str(self.damage) + ' ({0})'.format(self.get_damage()) + '\n'
		msg += 'defence: ' + str(self.defence) + ' ({0})'.format(self.get_defence()) + '\n'
		msg += 'charisma: ' + str(self.charisma) + ' ({0})'.format(self.get_charisma()) + '\n'
		msg += 'mana_damage: ' + str(self.mana_damage) + ' ({0})'.format(self.get_mana_damage()) + '\n'
		msg += 'intelligence: ' + str(self.intelligence) + ' ({0})'.format(self.get_intelligence()) + '\n'
		msg += 'visited_shop: ' + str(self.visited_shop) + '\n'
		msg += 'shop_items: ' + str(self.shop_items) + '\n'
		msg += 'shop_names: ' + str(self.shop_names) + '\n'
		msg += 'tags: ' + str(self.tags) + '\n'
		msg += 'room: ' + str(self.room) + '\n'
		msg += 'room_temp: ' + str(self.room_temp) + '\n'
		msg += 'reborn_answer: ' + str(self.reborn_answer) + '\n'
		msg += 'dead: ' + str(self.dead) + '\n'
		msg += 'rooms_to_story: ' + str(self.rooms_to_story) + '\n'
		msg += 'next_story_room: ' + str(self.next_story_room) + '\n'
		msg += 'subject: ' + str(self.subject)

		return msg

	def get_items(self):
		return [ i for i in [ itemloader.load_item(i[1], i[0]) for i in self.items ] if i is not None ]

	def get_damage(self):
		res = 0
		for i in self.get_items():
			res += i.damage

		return res + self.damage

	def get_damage_bonus(self, reply):
		res = 0
		for i in self.get_items():
			res += i.get_damage_bonus(self, reply)

		return res

	def get_defence(self):
		res = 0
		for i in self.get_items():
			res += i.defence

		return res + self.defence

	def get_charisma(self):
		res = 0
		for i in self.get_items():
			res += i.charisma

		return res + self.charisma

	def get_mana_damage(self):
		res = 0
		for i in self.get_items():
			res += i.mana_damage

		return res + self.mana_damage

	def get_intelligence(self):
		res = 0
		for i in self.get_items():
			res += i.intelligence

		return res + self.intelligence

	def has_aura(self, aura):
		for i in self.get_items():
			if i.aura == aura:
				return True
				
		return False

	def get_stats(self):
		return USER_STATS.format(self.hp, self.mp, self.gold)

	def remove_item(self, code_name):
		ind = -1
		for i in range(len(self.items)):
			if self.items[i][1] == code_name:
				ind = i
				break

		if ind >= 0:
			del self.items[ind]

	def remove_items_with_tag(self, tag):
		items = self.get_items()

		new_items = [ (i.buff, i.code_name) for i in items if tag not in i.tags ]

		self.items = new_items

	def remove_item_by_name(self, name):
		ind = -1
		items = self.get_items()
		for i in range(len(self.items)):
			if items[i].name == name:
				ind = i
				break

		if ind >= 0 and not items[ind].iscursed:
			del self.items[ind]

			return True
		return False

	def paid(self, costs):
		if self.gold >= costs and costs >= 0:
			self.gold -= costs

			return True
		else:
			return False

	def steal(self, price):
		self.gold = max(0, self.gold - price)

	def name_confirm(self, reply, text):
		if len(text) == 7:
			txt = NAME_CONFIRMED.format(self.name)
			self.state = 'first_msg'

			logger.info('New user with id {0}'.format(self.uid))

			reply(txt, [ WHATS_NEXT ])
		else:
			self.state = 'name'
			reply(ASK_NAME_AGAIN)

	def name_given(self, reply, name):
		if '_' in name:
			reply(NAME_ERROR)
		else:
			n = name
			while n == name:
				n = random.choice (names)

			msg = NAME_CONFIRM.format(n, name)

			buttons = [ NAME_AGREE, NAME_DISMISS ]
				
			self.state = 'name_confirm'
			self.name = name

			reply(msg, buttons)

	def make_damage(self, mn, mx, reply, death=True):
		old_hp = self.hp

		dmg = max(random.randint(mn, mx) - self.get_defence(), 0)
		self.hp -= dmg

		if not death:
			self.hp = max(self.hp, 1)
		elif self.hp <= 0:
			self.death(reply)

		return old_hp - self.hp

	def death(self, reply):
		self.dead = True
		self.state = ''

		reply(DEAD_MESSAGE, [ '/start' ])

	def open_corridor(self, reply):
		if self.state == 'room':
			for item in self.get_items():
				item.on_corridor(self, reply)

		self.state = 'corridor'
		reply(self.get_stats())

		buttons = [ OPEN_NEXT_DOOR, PLAYER_CHARACTERISTICS ]

		if not self.prayed:
			buttons.append(PRAY_TO_GOD)

		if not self.visited_shop:
			buttons.append(OPEN_SHOP)

		if len(self.items) > 0:
			buttons.append(SHOW_INVENTORY)

		reply(WHAT_WILL_WE_DO, buttons)

	def set_room_temp(self, name, val=None):
		self.room_temp[name] = val

	def get_room_temp(self, name, def_val=None):
		if name in self.room_temp:
			return self.room_temp[name]
		else:
			return def_val

	def get_fight_actions(self):
		actions = [
			KICK_ARM,
			KICK_MAGIC,
			USE + IMAGINATION
		]

		for i in self.get_items():
			if i.fightable:
				act = USE + i.name
				if act not in actions:
					actions.append(act)

		return actions

	def fight_dice(self, reply, result, subject=None):
		room = roomloader.load_room(self.room[1], self.room[0])
		if subject == 'noname':
			dmg = result + self.get_damage_bonus(reply) // 2

			reply(IMAGINATION_FIGHT.format(dmg))

			room.make_damage(self, reply, dmg)

			self.fight_answer(reply)


	def fight_action(self, reply, text):
		room = roomloader.load_room(self.room[1], self.room[0])
		if text == KICK_ARM:
			dmg = self.get_damage() + self.get_damage_bonus(reply)

			reply(MONSTER_DAMAGED.format(dmg))

			room.make_damage(self, reply, dmg)
		elif text == KICK_MAGIC:
			dmg = self.get_mana_damage()

			reply(MAGIC_KICKED.format(dmg))

			room.make_damage(self, reply, dmg)
		elif text.startswith(USE):
			name = text[len(USE):]
			item = None

			for i in self.get_items():
				if i.name == name:
					item = i
					break

			if item:
				dmg = item.fight_use(self, reply, room) + self.get_damage_bonus(reply)

				if item.disposable:
					self.remove_item(item.code_name)

				if self.state == 'room':
					reply(ITEM_USED.format(name, dmg))

					room.make_damage(self, reply, dmg)
			else:
				reply(NO_FIGHT_THING)

				self.throw_dice(reply, 'noname')
		else:
			reply(DIDNT_UNDERSTAND)

		if self.state == 'room':
			self.fight_answer(reply)

	def fight_answer(self, reply):
		room = roomloader.load_room(self.room[1], self.room[0])

		a, b = room.damage_range
		dmg = self.make_damage(a, b, reply)

		if not self.dead and dmg > 0.2:
			reply(USER_DAMAGED.format(dmg))

	def won(self, reply):
		room = roomloader.load_room(self.room[1], self.room[0])

		items = [ itemloader.load_item(i, 'loot') for i in room.loot ]
		loot = ', '.join([ item.name for item in items ]) if len(items) > 0 else 'Ничего.'

		for lt in room.loot:
			self.add_item('loot', lt)

		if room.coins > 0:
			reply(GOLD_FOUND.format(room.coins))

			self.gold += room.coins

		reply(YOU_WON.format(loot))

		self.leave(reply)

	def open_room(self, reply, room_type=None, room_name=None):
		self.state = 'room'

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

		reply(ROOM_OPENED)
		reply(room.name + '!')

		room.enter(self, reply)

		if self.state == 'room':
			reply(YOUR_ACTIONS, room.get_actions(self))

	def in_room(self, reply, text):
		room = roomloader.load_room(self.room[1], self.room[0])
		room.action(self, reply, text)

		if self.state == 'room':
			reply(self.get_stats())
			room = roomloader.load_room(self.room[1], self.room[0])
			reply(YOUR_ACTIONS, room.get_actions(self))

	def throw_dice(self, reply, subject=None):
		self.state = 'dice'
		self.subject = subject

		reply(DICE_TIME, [THOW_DICE])

	def get_dice_bonus(self, reply):
		res = 0

		for i in self.get_items():
			res += i.get_dice_bonus(self, reply)

		return res


	def dice(self, reply, text):
		if text == THOW_DICE:
			self.state = 'room'

			res = random.randint(1, DICE_MAX)
			res += self.get_dice_bonus(reply)
			reply(DICE_RESULT.format(res))
			
			room = roomloader.load_room(self.room[1], self.room[0])
			room.dice(self, reply, res, self.subject)

			if self.state == 'room':
				reply(YOUR_ACTIONS, room.get_actions(self))
		else:
			reply(DICE_CONFIDENCE, [THOW_DICE])

	def leave(self, reply):
		self.visited_shop = False
		self.prayed = False

		if self.hp < self.max_hp / 2:
			#reply('Ты слегка отдохнул')
			#self.hp = self.max_hp / 2
			pass

		self.open_corridor(reply)

	def escape(self, reply, success=True):
		for i in self.get_items():
			i.on_escape(self, reply, success)

		if success:
			self.leave(reply)
			
	def add_item(self, buff, name):
		self.items.append( (buff, name) )

	def add_tag(self, tag):
		self.tags.append(tag)

	def has_tag(self, tag):
		if tag in self.tags:
			return True

		#for i in self.get_items():
		#	if tag in i.tags:
		#		return True

		return False

	def remove_tag(self, tag):
		self.tags.remove(tag)

	def has_item(self, code_name):
		for i in self.items:
			if i[1] == code_name:
				return True

		return False

	def evilgod(self, reply, god):
		self.gods_level = [ 0 for g in self.gods ]

		if god == self.gods[0]: # Buddha
			txt = ()
			reply(EVIL_BUDDHA)
		elif god == self.gods[1]: # Jesus
			txt = ()
			self.make_damage(5, 10, reply, death=False)
			reply(EVIL_JESUS)
		elif god == self.gods[2]: # Allah
			self.make_damage(20, 30, reply)
			reply(EVIL_ALLAH)
		elif god == self.gods[3]: # Author
			self.add_item('special', 'intoxicated_shoes')
			
			reply(EVIL_AUTHOR)

	def god_love(self, reply, god):
		if god == BUDDHA_NUM: # Buddha
			reply(BUDDHA_LOVE)
			self.mp = self.max_mp
		elif god == JESUS_NUM: # Jesus
			reply(JESUS_LOVE)
			self.items.append(('special', 'wine'))
		elif god == ALLAH_NUM: # Allah
			reply(ALLAH_LOVE)
			self.hp = self.max_hp
		elif god == AUTHOR_NUM: # Author
			reply(AUTHOR_LOVE)
			self.open_room(reply, 'special', 'icecream')

	def prayto(self, reply, god):
		god_num = -1

		if god == self.gods[BUDDHA_NUM]: # Buddha
			reply(BUDDHA_PRAYED)
			god_num = BUDDHA_NUM
		elif god == self.gods[JESUS_NUM]: # Jesus
			reply(JESUS_PRAYED)
			god_num = JESUS_NUM
		elif god == self.gods[ALLAH_NUM]: # Allah
			reply(ALLAH_PRAYED)
			god_num = ALLAH_NUM
		elif god == self.gods[AUTHOR_NUM]: # Author
			reply(AUTHOR_PRAYED)
			god_num = AUTHOR_NUM
		else:
			reply(NO_GOD)

		if god_num >= 0:
			self.gods_level[god_num] += 1

			for item in self.get_items():
				item.on_pray(self, reply, god)


			if self.gods_level[god_num] >= GOD_LEVEL:
				self.god_love(reply, god_num)


		if self.state == 'pray':
			self.prayed = True
			self.open_corridor(reply)


	def pray(self, reply, god=None):
		self.state = 'pray'

		if god == None:
			if self.prayed:
				reply(FAST_GOD)
			else:
				reply(GOD_ASK, self.gods)
		elif god not in self.gods:
			reply(NO_GOD, self.gods)
		else:
			if len(self.last_god) > 0 and god != self.last_god:
				self.evilgod(reply, self.last_god)

			self.prayto(reply, god)
			self.last_god = god


	def open_shop(self, reply):
		self.state = 'shop'

		if self.visited_shop:
			self.open_corridor(reply)
			return

		self.shop_items = itemloader.load_shop_items()

		items =  [ itemloader.load_item(i[1], i[0]) for i in self.shop_items ]
		self.shop_names = [ i.name for i in items ]
		self.shop_names.append(EXIT)

		for item in self.get_items():
			item.on_shop(self, reply, items)

		txt = SHOP_MESSAGE.format(
			items[0].name, items[0].price, items[0].description, 
			items[1].name, items[1].price, items[1].description,
			items[2].name, items[2].price, items[2].description
		)

		reply(txt, self.shop_names)

	def buy(self, item, reply):
		if self.paid(item.price):
			if item.buff == 'bad':
				reply(BAD_BUYED)
			elif item.buff == 'good':
				reply(GOOD_BUYED)
			else:
				reply(NEUTRAL_BUYED)

			check = SHOP_CHECK.format(strftime("%Y-%m-%d %H:%M:%S UTC", gmtime()), item.name, item.price,)

			self.items.append((item.buff, item.code_name))
			item.on_buy(self, reply)
			reply(check)

			self.visited_shop = True
			self.open_corridor(reply)
		else:
			reply(NO_GOLD, self.shop_names)


	def shop(self, reply, text):
		if text == EXIT:
			reply(SHOP_EXITED)
			self.open_corridor(reply)
		else:
			for ind, name in enumerate(self.shop_names):
				if name == text:
					buff, name = self.shop_items[ind]
					item = itemloader.load_item(name, buff)
					self.buy(item, reply)
					return

			reply(NO_GOODS, self.shop_names)

	def open_inventory(self, reply):
		self.state = 'inventory'

		items = self.get_items()

		if len(items) == 0:
			self.open_corridor(reply)
			return

		actions = [ ]
		msg = INVENTORY_MESSAGE

		counter_items = Counter(items)
		selected_items = list(counter_items)

		begin = min(self.inventory_page * INVENTORY_PAGE_SIZE, len(selected_items) - 1)
		end = min((self.inventory_page + 1) * INVENTORY_PAGE_SIZE, len(selected_items))

		for i in selected_items[begin:end]:
			if i is not None:
				msg += '{0} ({1} шт.):\n{2}\n\n'.format(i.name, counter_items[i], i.description)
				if i.usable:
					actions.append(i.name)

				actions.append(THROW_AWAY + i.name)

		if begin > 0:
			actions.append(BACK)
		if end < len(selected_items):
			actions.append(NEXT)

		actions.append(TO_CORRIDOR)
		reply(msg, actions)

	def inventory(self, reply, text):
		if text == TO_CORRIDOR:
			self.open_corridor(reply)
		elif text.startswith(THROW_AWAY):
			name = text[len(THROW_AWAY):]

			if not self.remove_item_by_name(name):
				reply(CANT_THROW)
			else:
				self.open_inventory(reply)
		elif text == BACK:
			self.inventory_page = max(self.inventory_page - 1, 0)
			self.open_inventory(reply)
		elif text == NEXT:
			self.inventory_page = self.inventory_page + 1
			self.open_inventory(reply)
		else:
			items = self.get_items()
			
			for i in items:
				if i.name == text:
					i.on_use(self, reply)

					if i.disposable:
						self.remove_item(i.code_name)

					break
			
			if self.state == 'inventory':
				self.open_corridor(reply)

	def show_characteristics(self, reply):
		msg = CHARACTERISTICS.format(
			self.get_damage(), 
			self.get_defence(), 
			self.get_charisma(),
			self.get_mana_damage(),
			self.get_intelligence()
		)

		reply(msg)
		self.open_corridor(reply)

	def corridor(self, reply, text):
		if text.startswith(OPEN_NEXT_DOOR.split()[0]):
			self.open_room(reply)
		elif text.startswith(PRAY_TO_GOD.split()[0]):
			self.pray(reply)
		elif text.startswith(OPEN_SHOP.split()[0]):
			self.open_shop(reply)
		elif text.startswith(SHOW_INVENTORY.split()[0]):
			self.inventory_page = 0
			self.open_inventory(reply)
		elif text.startswith(PLAYER_CHARACTERISTICS.split()[0]):
			self.show_characteristics(reply)
		else:
			self.open_corridor(reply)


	def first(self, reply, text):
		reply(HELLO_MESSAGE)

		self.open_corridor(reply)

	def reborn(self, reply, answer):
		self.state = 'reborned'
		self.reborn_answer = answer

	def message(self, reply, text):
		if self.dead:
			reply(DEAD_MESSAGE_AGAIN, [ '/start' ])
		elif self.state == 'name':
			self.name_given(reply, text)
		elif self.state == 'name_confirm':
			self.name_confirm(reply, text)
		elif self.state == 'first_msg':
			self.first(reply, text)
		elif self.state == 'corridor':
			self.corridor(reply, text)
		elif self.state == 'pray':
			self.pray(reply, text)
		elif self.state == 'shop':
			self.shop(reply, text)
		elif self.state == 'inventory':
			self.inventory(reply, text)
		elif self.state == 'room':
			self.in_room(reply, text)
		elif self.state == 'dice':
			self.dice(reply, text)
		elif self.state == 'reborned':
			reply(self.reborn_answer, [ '/start' ])
			
