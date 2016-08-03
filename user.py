import random
from utils.names import names

class User(object):
	def __init__(self, uid):
		super(User, self).__init__()

		self.uid = uid

		self.name = 'none'
		self.hp = 100
		self.mp = 100

		self.state = 'name'

		self.gods = [ 'Будда', 'Христос', 'Аллах', 'Рассказчик' ]
		self.gods_level = [ 0 for g in self.gods ]
		self.last_god = ''
		self.prayed = False

		self.room = ''

	def get_stats(self):
		return 'HP: {0} MP: {1}'.format(self.hp, self.mp)

	def name_confirm(self, reply, text):
		if len(text) == 7:
			txt = ('Твоя взяла. Отныне и навсегда (Нет) '
					'тебя будут звать «{0}». Поменять имя '
					'можно с помощью /setname').format(self.name)
			self.state = 'first_msg'

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

	def damage(self, mn, mx, death=True):
		dmg = random.randint(mn, mx)
		self.hp -= dmg

		if not death:
			self.hp = 1

	def open_corridor(self, reply):
		self.state = 'corridor'
		reply(self.get_stats())

		buttons = [ 'Открыть очередную дверь', 'Зайти в Магазин алхимика' ]

		if not self.prayed:
			buttons.append('Молить Бога о выходе')

		reply('Что будем делать?', buttons)

	def open_room(self, reply):
		reply('Not implemented')

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
			self.damage(5, 10, death=False)
			reply(txt)
		elif god == self.gods[2]: # Allah
			txt = ('Аллах не терпит ошибок и он очень зол.')
			self.damage(20, 30)
			reply(txt)
		elif god == self.gods[3]: # Author
			txt = ('Ты же понимаешь, что я тут заправляю всем и могу отправить '
					'тебя к какому-нибудь дракону?')

			# TODO: Open dragon
			reply(txt)

	def prayto(self, reply, god):
		self.gods_level[self.gods_level.index(god)] += 1


		if god == self.gods[0]: # Buddha
			reply('Не хочу тебя расстраивать, но буддисты не молятся')			
		elif god == self.gods[1]: # Jesus
			reply('Продолжай в том же духе и мы сможем пройти по воде')			
		elif god == self.gods[2]: # Allah
			reply('Аллах не терпит ошибок.')			
		elif god == self.gods[3]: # Author
			reply('Ох как приятно. Спасибо тебе')	

		self.prayed = True
		selp.open_corridor(reply)


	def pray(self, reply, god=None):
		self.state = 'pray'
		
		if god == None:
			if self.prayed:
				reply('Не так часто, Боги не любят культивистов.')
			else:
				reply('Ну и кому в этот раз?', self.gods)
		elif god not in self.gods:
			reply('Для такого нет оборудования?', self.gods)
		else:
			if len(self.last_god) > 0 and god != self.last_god:
				self.evilgod(self.last_god)

			self.prayto(reply, god)
			self.last_god = god


	def shop(self, reply):
		reply('Not implemented')

	def corridor(self, reply, text):
		if text.startswith('Открыть'):
			self.open_room(reply)
			self.open_corridor(reply)
		elif text.startswith('Молить'):
			self.pray(reply)
		elif text.startswith('Зайти'):
			self.shop(reply)
			self.open_corridor(reply)


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
			'требущее удачи и мастерства.'
			'Ну или по крайней мере расмешат твоих противьников неудачным '
			'броском.')


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