name = 'Зеркало'

actions = [ 'Разбить', 'Уйти с миром' ]

next_story_room_range = (100000000000000, 200000000000000)
next_story_room = 'none'

def get_actions(user):
	return actions

def enter(user, reply):
	reply('Сюжетное зеркало')
	reply('Отомстить?')

def action(user, reply, text):
	if text == actions[0]:
		reply('Ты разбил его и пробудил духа...')
	
	user.leave(reply)