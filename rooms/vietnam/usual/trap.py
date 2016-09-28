from utils.buffs import VietnamBuff

name = 'Листва'

def enter(user, reply):
	reply(
		'Не дойдя пары шагов до двери, ты с грохотом проваливаешься '
		'в яму, на дне которой хищно поблескивает огромный капкан. '
		'Стальные челюсти захлопываются на твоих ногах. Чёрт! '
		'Надо выбираться. '
	)

def get_actions(user):
	return [ 'Выбираться' ]

def action(user, reply, text):
	user.new_buff(VietnamBuff())
	user.leave(reply)