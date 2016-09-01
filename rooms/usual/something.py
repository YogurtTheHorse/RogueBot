import random
import usermanager
from constants import *

TOOK_TOOK = 'Отдышаться и вежливо постучать в дверь'
SPINE = 'Войти спиной вперёд'

QUESTION_KODZIMA = '—А... э-э... как Вы здесь оказались?'

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
			msg = (
				'—Проходи, {0}, чего хотел?\nНа негнущихся коленях Вы проходите в середину комнаты. '
				'Да, глаза Вас не подвели, это действительно...\n*Хидэо Кодзима*!'
			).format(user.name)

			reply(msg)
			user.set_room_temp('question', 'kodzima')
		elif text == SPINE:
			reply('Начав движение, из-за спины Вы слышите голос с небольшим восточным акцентом:—Ты что, идиот?')
			user.set_room_temp('question', 'spine')
	elif question == 'kodzima':
		if text == QUESTION_KODZIMA:
			user1 = usermanager.random_user()
			user2 = usermanager.random_user()
			name1 = user1.name
			name2 = user2.name

			reply('—Так же, как и ты, очевидно же. Всё, не занимай линию, там за тобой уже двое в очереди. {0} и {1}, чёрт бы его побрал, уже третий раз за сегодня'.format(name1, name2))
		else:
			reply('От волнения Вы не придумали ничего лучше, как рассказать анекдот собственного сочинения.\n—Заходит как-то геймдизайнер в бар, \n—бодро начинаете Вы, но неожиданно с Вашим лицом резко стыкуется табурет, на котором недавно сидел Хидэо:—Пошёл вон!')
			user.make_damage(25, 50, reply, False)

		reply('Тебя выставили за дверь')
		user.leave(reply)
	elif question == 'spine':
		reply('Вы испытываете сильный стыд и так краснеете, что на лице лопается капилляр.')
		user.make_damage(10, 15, reply, False)

		user.leave(reply)

def get_actions(user):
	question = user.get_room_temp('question', def_val='first')
	ans = [ ]

	if question == 'first':
		ans = [ TOOK_TOOK, SPINE ]
	elif question == 'kodzima':
		ans = [ QUESTION_KODZIMA, 'Рассказать анекдот' ]
	else:
		ans = [ 'Я... э-э... (сбежать)' ]

	return ans