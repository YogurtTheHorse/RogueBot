name = 'Конец игры'

def get_actions(user):
	return [ 'Выйти на поверхность', 'Уйти' ]

def enter(user, reply):
	reply('Трава, облачка, птички щебечут! Неужели ты нашел выход? Мы выбрались отсюда!')

def action(user, reply, text):
	if text == 'Выйти на поверхность':
		user.death(reply, reason='Конец игры')
	else:
		user.leave(reply)