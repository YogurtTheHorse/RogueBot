name = 'Старик'

actions = [ 'Помолчать', 'Уйти' ]

def get_actions(user):
	return actions

def enter(user, reply):
	reply('Опасно идти одному! Возьми это.')

	user.add_item('neutral', 'bullet')
	user.add_item('story', 'gun')
	user.add_item('story', 'glasses')


	reply('_Какой-то сверток.. Посмотрю потом, как выйду от сюда. Этот старик подозрительно молчит_')

def action(user, reply, text):
	if text == actions[0]:
		reply('_тишина_')
	else:
		user.leave(reply)