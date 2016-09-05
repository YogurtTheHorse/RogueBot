import random

name = 'Не видно'

def get_actions(user):
	return [ 'Идти дальше' ]

def enter(user, reply):
	reply('Ты видишь ' + random.choice(['Лес', 'Дорога', 'Дупло', 'Ничего', 'Мама']))

def action(user, reply, text):
	user.open_room(reply)