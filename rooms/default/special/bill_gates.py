from localizations import locale_manager
import random
import usermanager
from constants import *

CONFUSED = locale_manager.get('rooms.default.special.bill_gates.phrase_2')
SPINE = locale_manager.get('rooms.default.special.bill_gates.phrase_3')

name = locale_manager.get('rooms.default.special.bill_gates.phrase_4')

def enter(user, reply):
	msg = (
		locale_manager.get('rooms.default.special.bill_gates.phrase_1')
	)
	reply(msg.format(user.name))
	user.set_room_temp('question', 'first')

def action(user, reply, text):
	question = user.get_room_temp('question', def_val='first')

	if question == 'first':
		reply(locale_manager.get('rooms.default.special.bill_gates.phrase_5'))
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
		ans = [ locale_manager.get('rooms.default.special.bill_gates.phrase_6') ]
	else:
		ans = [ locale_manager.get('rooms.default.special.bill_gates.phrase_7') ]

	return ans