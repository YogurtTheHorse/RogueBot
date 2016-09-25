name = 'Нечто из глубин'

hp = 900
damage_range = ( 40, 80 )

coins = 900
loot = [ 'puzzle' ]
is_monster = True

def enter(user, reply):
	reply('Ужас забирается в твоё сознание...')

	if user.rooms_count < 800:
		reply('...и берёт тебя под контроль. Ты так и не понял, что произошло, но твои ноги тебя вынесли из комнаты. Сами.')
		user.leave(reply)
	else:
		reply('...но чудищу не удалось захватить твой разум и теперь оно злится.')

def get_actions(user):
	return user.get_fight_actions()

def action(user, reply, text):
	user.fight_action(reply, text)	