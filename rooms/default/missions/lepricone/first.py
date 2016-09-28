name = 'Леприкон'
damage_range = (25, 50)
hp = 1500
loot = [ 'clever' ]

is_monster = True

def enter(user, reply):
	reply('Набежали процентики.. Он требует *1000* золотых.')

def get_actions(user):
	acts = user.get_fight_actions()

	if user.gold >= 1000:
		acts = [ 'Вернуть долг' ] + acts

	return acts

def action(user, reply, text):
	if text == 'Вернуть долг' and user.gold >= 1000:
		user.gold -= 1000
		user.leave(reply)
	else:
		user.fight_action(reply, text)
