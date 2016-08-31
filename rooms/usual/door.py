name = 'Дверь'

actions = [ 'Постоять', 'Открыть' ]

def get_actions(user):
	return actions

def enter(user, reply):
	reply('Дубовая!')

def action(user, reply, text):
	if text == actions[0]:
		reply('_тишина_')
	else:
		reply('Ты открываешь дверь, а за ней.. Коридор!')
		user.leave(reply)