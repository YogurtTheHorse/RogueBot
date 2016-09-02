name = 'Старик'

actions = [ 'Помолчать', 'Уйти' ]

next_story_room_range = (20, 30)
next_story_room = 'second'

def get_actions(user):
	return actions

def enter(user, reply):
	reply('Опасно идти одному! Возьми это.')

	user.add_item('story', 'gun')
	user.add_item('story', 'map')
	user.add_item('neutral', 'bullet')
	user.add_item('story', 'glasses')

	reply('_Какой-то сверток..\nПосмотрю потом, как выйду отсюда. Этот старик подозрительно молчит_')

def action(user, reply, text):
	if text == actions[0]:
		reply('_тишина_')
	else:
		user.leave(reply)