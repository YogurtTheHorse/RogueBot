name = 'Собачка'

def get_actions(user):
	return [ ]

def enter(user, reply):
	reply('Она хочет к тебе!')
	user.new_pet(reply, 'dog')

def action(user, reply, text):
	user.leave(reply)