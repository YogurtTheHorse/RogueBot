name = 'Старик'

actions = [ 'Помолчать', 'Уйти' ]

def get_actions(user):
	return actions

def enter(user, reply):
	reply('_Какой-то сверток..\nПосмотрю потом, как выйду отсюда. Этот старик подозрительно молчит_')
	user.new_mission('main', 'second', 10)

def action(user, reply, text):
	if text == actions[0]:
		reply('_тишина_')
	else:
		user.leave(reply)