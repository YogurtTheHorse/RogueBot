import random
import logging
from utils.names import names

class User(object):
	def __init__(self, uid):
		super(User, self).__init__()

		self.uid = uid

		self.name = 'none'
		self.hp = 100
		self.mp = 100

		self.state = 'name'

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

	def open_corridor(self, reply):
		self.state = 'corridor'
		reply(self.get_stats())

		buttons = [ 'Открыть очередную дверь', 'Молить Бога о выходе', 'Зайти в Магазин алхимика' ]

		reply('Что будем делать?', buttons)

	def corridor(self, reply, text):
		reply('Not implemented')

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