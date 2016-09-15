from constants import *

FIGHT = 'Наброситься на коротышку'

name = 'Гидеон'

def enter(user,reply):
	reply('Признай, без этой книжки ты никто. Нет ни силы, ни ума.\n И что ты сделаешь?\n Что ты сделаешь?')
	user.throw_dice(reply)

def dice(user, reply, result, subject=None):
	if result > DICE_MAX:
		reply('Что-о-о? Как ты это сделал?')
		if not user.has_item('mystery_book_2'):
			reply('От шока Гидеон выронил дневник из рук.')
			user.add_item('special', 'mystery_book_2')
		user.leave(reply)
	else:
		reply('Ничего ты не можешь!')
		user.leave(reply)

def get_actions(user):
	return []

def action(user, reply, text):
	pass