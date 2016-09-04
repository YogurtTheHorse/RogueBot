name = 'Веган'

actions = [ 'Постоять', 'Уйти' ]

def get_actions(user):
	return actions

def enter(user, reply):
	reply('—Я веган!')

def action(user, reply, text):
	if text == actions[0]:
		reply('—Я веган!')
	else:
		reply('Ты возвращаешься в коридор!')
		user.leave(reply)