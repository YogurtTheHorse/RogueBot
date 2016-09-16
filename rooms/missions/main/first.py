name = 'Старик'

actions = [ 'Помолчать', 'Уйти' ]

def get_actions(user):
	return actions

def enter(user, reply):
	reply('_Какой-то сверток..\nПосмотрю потом, как выйду отсюда. Этот старик подозрительно молчит._')

	user.add_item('story', 'gun')
	user.add_item('story', 'map')
	user.add_item('neutral', 'bullet')
	user.add_item('story', 'glasses')


	user.new_mission('main', 'second', 10)

def action(user, reply, text):
	if text == actions[0]:
		reply('_тишина_')
	else:
		user.leave(reply)