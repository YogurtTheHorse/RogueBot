name = 'Отдел кадров'

def get_actions(user):
	return [ 'Уйти' ]

def enter(user, reply):
	reply('— Мы вам перезвоним!')

def action(user, reply, text):
	user.leave(reply)