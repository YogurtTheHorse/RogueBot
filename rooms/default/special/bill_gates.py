import random
import usermanager
from constants import *

CONFUSED = 'Растеряться'
SPINE = 'Войти спиной вперёд'

name = 'Человек'

def enter(user, reply):
	msg = (
		'—Проходи, {0}, чего хотел?\n\nНа негнущихся коленях ты проходишь '
		'в середину комнаты. Да, глаза не подвели, это действительно...\n\n'
		'*Билл Гейтс*!'
	)
	reply(msg.format(user.name))
	user.set_room_temp('question', 'first')

def action(user, reply, text):
	question = user.get_room_temp('question', def_val='first')

	if question == 'first':
		reply('—Ты чего там стоишь как не родной? Хочешь фокус? Следи за руками... Опа!')
		reply('*ВАШЕ УСТРОЙСТВО ОБНОВЛЕНО ДО WINDOWS 10*')
		user.set_room_temp('question', '14')
	elif question == '14':
		reply('Загрузка... 14%')
		user.set_room_temp('question', '36')
	elif question == '36':
		reply('Загрузка... 36%')
		user.set_room_temp('question', '28')
	elif question == '28':
		reply('Загрузка... 28%')
		user.set_room_temp('question', '74')
	elif question == '74':
		reply('Загрузка... 74%')
		user.set_room_temp('question', '97')
	elif question == '97':
		reply('Загрузка... 97%')
		user.set_room_temp('question', '99')
	elif question == '99':
		reply('Загрузка... 99%')
		user.set_room_temp('question', 'error')
	else:
		reply('*Ошибка 0х000009с*')
		user.leave(reply)

def get_actions(user):
	question = user.get_room_temp('question', def_val='first')
	ans = [ ]

	if question == 'first':
		ans = [ 'Растеряться' ]
	else:
		ans = [ 'Загрузка' ]

	return ans