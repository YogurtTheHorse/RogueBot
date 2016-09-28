import random
import usermanager
from constants import *

TOOK_TOOK = 'Отдышаться и вежливо постучать в дверь'
SPINE = 'Войти спиной вперёд'

name = 'Человек'

def enter(user, reply):
	msg = (
		'Вы заходите в комнату и, бросив мимолётный взгляд на человека, сидящего '
		'в уголке на табурете, непринуждённо поворачиваете на сто восемьдесят '
		'градусов и выходите за дверь. Зачем-то при этом насвистывая что-то из раннего Моцарта.'
	)
	reply(msg)
	user.set_room_temp('question', 'first')

def action(user, reply, text):
	question = user.get_room_temp('question', def_val='first')

	if question == 'first':
		if text == TOOK_TOOK:
			rnd = random.random()
			if rnd < 0.20:
				user.open_room(reply, 'special', 'kiba')
			elif rnd < 0.40:
				user.open_room(reply, 'special', 'kodzima')
			elif rnd < 0.60:
				user.open_room(reply, 'special', 'gabe')
			elif rnd < 0.80:
				user.open_room(reply, 'special', 'yegorf1')
			else:
				user.open_room(reply, 'special', 'bill_gates')
		elif text == SPINE:
			reply('Начав движение, из-за спины Вы слышите голос с небольшим восточным акцентом: — Ты что, идиот?')
			user.set_room_temp('question', 'spine')
	elif question == 'spine':
		reply('Вы испытываете сильный стыд и так краснеете, что на лице лопается капилляр.')
		user.make_damage(10, 15, reply, False)

		user.leave(reply)

def get_actions(user):
	question = user.get_room_temp('question', def_val='first')
	ans = [ ]

	if question == 'first':
		ans = [ TOOK_TOOK, SPINE ]
	else:
		ans = [ 'Я... э-э... (сбежать)' ]

	return ans