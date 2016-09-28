name = 'Горшок золота'

def on_enter(user, reply):
	reply(
		'Вы входите на полянку, устланную четырехлистными клеверами. '
		'В центре стоит горшочек, полный золота. Что это над ним? Радуга? '
		'Откуда она, черт возьми в подземелье ? Хотя какая разница, '
		'когда перед тобой столько золота!'
	)

def get_actions(user):
	return [ 'Взять золото', 'Уйти' ]

def action(user, reply, text):
	if text == 'Взять золото':
		user.gold += 250
		user.new_mission('lepricone', path_len=7)
		reply('О, 250 монет!')

	user.leave(reply)
