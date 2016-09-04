import random

name = random.choice(['Лес', 'Дорога', 'Дупло', 'Ничего', 'Мама'])

def get_actions(user):
	return [ 'Идти дальше' ]

def enter(user, reply):
	reply('Что?')

def action(user, reply, text):
	user.open_room(reply)