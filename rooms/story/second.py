name = 'Сэр Качкалот'

actions = [ 'Помолчать', 'Уйти' ]

next_story_room_range = (15, 25)
next_story_room = 'third'

def get_actions(user):
	return actions

def enter(user, reply):
	reply('—А.. Э.. Это же не спортзал.')
	reply('—Верно, это сюжетная линия. Автор попросил меня постоять здесь.')

	if user.charisma > 10:
		reply('В общем-то ты можешь идти дальше')
		next_story_room = 'second'
	else:
		reply('Ты какой-то некрасивый. Я тебя не пущу. Ты себя в зеркале видел?')

def action(user, reply, text):
	if text == actions[0]:
		reply('А ну проваливай!')
	else:
		user.leave(reply)