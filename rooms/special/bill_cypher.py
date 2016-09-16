ESCAPE = 'Забирай, они мне не нужны'
READY = 'А что я получу взамен?'
FIGHT = 'Я не отдам их демону!'

name = 'Билл Шифр'

def enter(user, reply):
	msg = (
		'Вы оказались в странном измерении, кажется здесь нет постоянства.\n'
		'Ваше внимание привлек большой желтый треугольник с глазом посередине,\n'
		'который пристально на вас смотрит.\n'
		'Ты славно потрудился, что принёс их сюда, а теперь отдай их.'
	)
	reply(msg)

	user.set_room_temp('question', 'first')

def get_actions(user):
	question = user.get_room_temp('question', def_val='first')
	
	if question == 'first':
		return [ ESCAPE, READY, FIGHT ]
	else:
		return [ 'Да, забирай!', 'Что еще предложишь?' ]

def action(user, reply, text):
	question = user.get_room_temp('question', def_val='first')

	if question == 'first':
		if text == ESCAPE:
			reply('Хороший мальчик, а теперь прощай!')
			user.max_hp += 20
			user.leave(reply)
		elif text == READY:
			reply('Я думаю это тебя убедит. Здесь 4000 золотых.')
			user.set_room_temp('question', 'negotiate')
		elif text == FIGHT:
			reply('Посмотри на себя, зачем так злиться?.\nТеперь ты зеркало.')
			user.reborn(reply, 'Зеркало может только отражать.', name='Зеркало')
	elif question == 'negotiate':
		if text == 'Да, забирай!':
			reply('Вот и славно. Смотри не рассыпь.')
			user.gold += 4000
			user.leave(reply)
		else:
			reply('Какой ты не сговорчивый.\nСловно воды в рот набрал.')
			user.reborn(reply, 'Рыбы на суше не живут.', name='Рыба')
