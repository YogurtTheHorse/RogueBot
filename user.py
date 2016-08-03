import random

from time import gmtime, strftime

import items.itemloader as itemloader

import logging
from constants import *
from utils.names import names

logger = logging.getLogger('rg')

class User(object):
	def __init__(self, uid):
		super(User, self).__init__()

		self.uid = uid

		self.name = 'none'
		self.hp = 100
		self.mp = 100
		self.gold = 10 ** 7

		self.state = 'name'

		self.items = [ ]

		self.gods = [ BUDDHA, JESUS, ALLAH, AUTHOR ]
		self.gods_level = [ 0 for g in self.gods ]
		self.last_god = ''
		self.prayed = False

		self.damage = 1
		self.defence = 1
		self.charisma = 0
		self.mana_damage = 0
		self.intelligence = 0

		self.visited_shop = False
		self.shop_items = [ ]
		self.shop_names = [ ]

		self.room = ''

	def debug_info(self):
		msg = 'uid: ' + str(self.uid) + '\n'
		msg += 'name: ' + str(self.name) + '\n'
		msg += 'hp: ' + str(self.hp) + '\n'
		msg += 'mp: ' + str(self.mp) + '\n'
		msg += 'gold: ' + str(self.gold) + '\n'
		msg += 'state: ' + str(self.state) + '\n'
		msg += 'items: ' + str(self.items) + '\n'
		msg += 'gods: ' + str(self.gods) + '\n'
		msg += 'gods_level: ' + str(self.gods_level) + '\n'
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
		msg += 'room: ' + str(self.room)

		return msg

	def get_items(self):
		return [ itemloader.load_item(i[1], i[0]) for i in self.shop_items ]

	def get_damage(self):
		res = 0
		for i in self.get_items():
			res += i.damage

		return res + self.damage

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

	def get_stats(self):
		return 'HP: {0} MP: {1} Gold: {2}'.format(self.hp, self.mp, self.gold)

	def name_confirm(self, reply, text):
		if len(text) == 7:
			txt = ('Твоя взяла. Отныне и навсегда (Нет) '
					'тебя будут звать «{0}». Поменять имя '
					'можно с помощью /setname').format(self.name)
			self.state = 'first_msg'

			logger.info('New user with id {0}'.format(self.uid))

			reply(txt, [ 'А что дальше?' ])
		else:
			self.state = 'name'
			reply('Ну и как же тебя звать на этот раз?')

	def name_given(self, reply, name):
		n = random.choice (names)
		msg = ('Ты знаешь, у меня есть знакомый по имени «{0}» и '
				'я считаю, что это звучит лучше «{1}»\n'
				'Ты уверен?').format(n, name)

		buttons = [ 'Уверен.', 'Дай-ка я поменяю.' ]
			
		self.state = 'name_confirm'
		self.name = name

		reply(msg, buttons)

	def make_damage(self, mn, mx, death=True):
		dmg = random.randint(mn, mx)
		self.hp -= dmg

		if not death:
			self.hp = max(self.hp, 1)

	def open_corridor(self, reply):
		if self.state == 'room':
			for item in self.get_items():
				item.on_corridor(self, reply)

		self.state = 'corridor'
		reply(self.get_stats())

		buttons = [ 'Открыть очередную дверь' ]

		if not self.prayed:
			buttons.append('Молить Бога о выходе')

		if not self.visited_shop:
			buttons.append('Зайти в Магазин алхимика')

		if len(self.items) > 0:
			buttons.append('Посмотреть инвентарь')

		reply('Что будем делать?', buttons)

	def open_room(self, reply):
		reply('Not implemented')
		reply('Магазин и молитвы снова дозволены')

		self.visited_shop = False
		self.prayed = False

	def evilgod(self, reply, god):
		self.gods_level = [ 0 for g in self.gods ]

		if god == self.gods[0]: # Buddha
			txt = ('Тебе повезло, что Буддисты полны спокойствия и не злятся, '
					'когда кто-то меняет Веру. Им вообще пофиг. На _все_.')
			reply(txt)
		elif god == self.gods[1]: # Jesus
			txt = ('Иисус разгневался и убил всех твоих египтских детей. '
					'Правда у тебя их не было, но это событие так растрогало '
					'тебя, что ты потерял частичку себя.')
			self.make_damage(5, 10, death=False)
			reply(txt)
		elif god == self.gods[2]: # Allah
			txt = ('Аллах не терпит ошибок и он очень зол.')
			self.make_damage(20, 30)
			reply(txt)
		elif god == self.gods[3]: # Author
			txt = ('Ты же понимаешь, что я тут заправляю всем и могу отправить '
					'тебя к какому-нибудь дракону?')

			# TODO: Open dragon
			reply(txt)

	def god_love(self, reply, god):
		if god == BUDDHA_NUM: # Buddha
			reply('Ты обрел частичку Нирваны, парень.')
			self.mp = self.max_mp
		elif god == JESUS_NUM: # Jesus
			reply('Твой рюкзак потяжелел.. Хм.. Странно')
			self.items.append(('special', 'wine'))
		elif god == ALLAH_NUM: # Allah
			reply('Ты чувствуешь как силы приходят к тебе!')
			self.hp = self.max_hp
		elif god == AUTHOR_NUM: # Author
			reply('За это я подскажу тебе одну интересную комнату')
			reply('Not implemented')

	def prayto(self, reply, god):
		god_num = -1

		if god == self.gods[BUDDHA_NUM]: # Buddha
			reply('Не хочу тебя расстраивать, но буддисты не молятся')
			god_num = BUDDHA_NUM
		elif god == self.gods[JESUS_NUM]: # Jesus
			reply('Продолжай в том же духе и мы сможем пройти по воде')
			god_num = JESUS_NUM
		elif god == self.gods[ALLAH_NUM]: # Allah
			reply('Аллах не терпит ошибок.')
			god_num = ALLAH_NUM
		elif god == self.gods[AUTHOR_NUM]: # Author
			reply('Ох как приятно. Спасибо тебе')	
			god_num = AUTHOR_NUM
		else:
			reply('Таких не молим.')

		if god_num >= 0:
			self.gods_level[god_num] += 1

			for item in self.get_items():
				item.on_pray(self, reply, god)


			if self.gods_level[god_num] >= GOD_LEVEL:
				self.god_love(reply, god_num)


		self.prayed = True
		self.open_corridor(reply)


	def pray(self, reply, god=None):
		self.state = 'pray'

		if god == None:
			if self.prayed:
				reply('Не так часто, Боги не любят культивистов.')
			else:
				reply('Ну и кому в этот раз?', self.gods)
		elif god not in self.gods:
			reply('Для такого нет оборудования', self.gods)
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

		items = self.get_items()
		self.shop_names = [ i.name for i in items ]

		for item in self.get_items():
			item.on_shop(self, reply, items)

		txt = (
			'Привет! Давно не виделись, смотри, что у меня есть:\n\n'
			'{0}\nЦена: {1}\n{2}\n\n'
			'{3}\nЦена: {4}\n{5}\n\n'
			'{6}\nЦена: {7}\n{8}'
		).format(
			items[0].name, items[0].price, items[0].description, 
			items[1].name, items[1].price, items[1].description,
			items[2].name, items[2].price, items[2].description
		)

		reply(txt, self.shop_names)

	def buy(self, item, reply):
		if self.gold >= item.price:
			self.gold -= item.price
			if item.buff == 'bad':
				reply('Ну наконец-то кто-то это купил!')
			elif item.buff == 'good':
				reply('Хороший выбор')
			else:
				reply('Забирай скорей')

			check = ( '```text'
				'         ООО "Магазин подземелья"         \n'
				'             ДОБРО ПОЖАЛОВАТЬ!            \n'
				'Покупка: {0}\n'
				'Кассир: №1\n\n'
				'------------------------------------------\n\n'
				'ПРОДАЖА\n'
				'  {1} 1 шт. — {2}.00 злт\n'
				'\n'
				'ИТОГО — {2}.00 злт\n'
				'\nСпасибо за покупку!\n'
				'```'
			).format(strftime("%Y-%m-%d %H:%M:%S UTC", gmtime()), item.name, item.price,)

			self.items.append((item.buff, item.code_name))
			item.on_buy(self, reply)
			reply(check)

			self.visited_shop = True
			self.open_corridor(reply)
		else:
			reply('Нет денег — нет товара!')


	def shop(self, reply, text):
		for ind, name in enumerate(self.shop_names):
			if name == text:
				buff, name = self.shop_items[ind]
				item = itemloader.load_item(name, buff)
				self.buy(item, reply)
				return

		reply('У меня такого нет')

	def open_inventory(self, reply):
		self.state = 'inventory'

		items = self.get_items()

		actions = [ ]
		msg = ''

		for i in items:
			msg += '{0}:\n{1}\n\n'.format(i.name, i.description)
			if i.usable:
				actions.append(i.name)

		if len(actions) > 0:
			actions.append('В коридор')
			reply(msg, actions)
		else:
			reply(msg)
			self.open_corridor(reply)


	def inventory(self, reply, text):
		if text == 'В коридор':
			self.open_corridor(reply)
		else:
			items = self.get_items()
			
			for i in items:
				if i.name == text:
					i.on_use(self, reply)
			
			self.open_corridor()

	def corridor(self, reply, text):
		if text.startswith('Открыть'):
			self.open_room(reply)
			self.open_corridor(reply)
		elif text.startswith('Молить'):
			self.pray(reply)
		elif text.startswith('Зайти'):
			self.open_shop(reply)
		elif text.startswith('Посмотреть'):
			self.open_inventory(reply)


	def first(self, reply, text):
		txt = (''
			'Ты начинаешь сложный путь, а я твой рассказчик. Сейчас ты стоишь '
			'посреди коридора - центр нашей с тобой игры. В нем множество '
			'разных дверей и каждый ход ты будешь открывать одну из них. Есть '
			'ли выход из этого ада я, честно говоря, не знаю, но мы можем '
			'проверить.\n\n'
			'Будь осторожен, за дверью может оказать подземелье с драконом, '
			'хотя с такой же вероятностью и озеро мороженного.\n\n'
			'Держи игральные кости, их нужно будет кидать каждое действие, '
			'требущее удачи и мастерства. При хорошем броске монстр падет.'
			'А при неудаче.. Могут расмешить твоих противьников и они '
			'сжалятся над тобой.')


		reply(txt)

		self.open_corridor(reply)

	def message(self, reply, text):
		if self.state == 'name':
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