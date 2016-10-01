import random

name = 'Подсказка'

tips = [
	'Если смотреть на то, что говорит алхимик, то можно понять, хорошую вещь ты купил или нет.',
	'Смерть и жизнь едины, а значит конец это не конец. Но лучше не заканчивать.',
	'Лучше спилить мушку',
	'Иногда не стоит читать до конца, можно понять суть раньше',
	'Старайся бить зеркало не сильно и не умрешь. _Так быстро_',
	'Не доверяй красоткам'
]

actions = [ 'Послушать и уйти', 'У вас подсказки не интересные' ]

def get_actions(user):
	return actions

def enter(user, reply):
	reply('Спойлеры?')

def action(user, reply, text):
	if text == actions[0]:
		reply(random.choice(tips))

		user.new_mission('tips', 'tips', path_len=25)
	else:
		reply('Ну и проваливай!')
	user.leave(reply)