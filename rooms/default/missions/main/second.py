name = 'Сэр Качкалот'

actions = [ 'Помолчать', 'Уйти' ]

def get_actions(user):
	return actions

def enter(user, reply):
	reply('—А.. Э.. Это же не спортзал.')
	reply('—Верно, это сюжетная линия. Автор попросил меня постоять здесь.')

	if user.get_charisma() > 10:
		reply('В общем-то ты можешь идти дальше.')
		user.new_mission('main', 'third', 15)
	else:
		reply('Ты какой-то некрасивый. Я тебя не пущу. Ты себя в зеркале видел?')
		user.new_mission('main', 'second', 15)

def action(user, reply, text):
	if text == actions[0]:
		reply('А ну проваливай!')
	else:
		user.leave(reply)