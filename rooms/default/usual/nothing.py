import random

name = random.choice(['Лес', 'Дорога', 'Дупло', 'Ничего', 'Мама'])
not_for_sign = True

def get_actions(user):
	return [ 'Идти дальше' ]

def enter(user, reply):
	reply('Удивительно')

def action(user, reply, text):
	user.open_room(reply)
