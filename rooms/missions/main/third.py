name = 'Зеркало'

actions = [ 'Разбить', 'Уйти с миром' ]

def get_actions(user):
	return actions

def enter(user, reply):
	reply('Сюжетное зеркало.')
	reply('Отомстить?')

def action(user, reply, text):
	if text == actions[0]:
		reply('Ты разбил его и пробудил духа...')
	
	user.leave(reply)