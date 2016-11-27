from localizations import locale_manager
name = locale_manager.get('rooms.vietnam.missions_lepricone.first.phrase_1')
damage_range = (25, 50)
hp = 1500
loot = [ 'clever' ]

is_monster = True

def enter(user, reply):
	reply(locale_manager.get('rooms.vietnam.missions_lepricone.first.phrase_2'))

def get_actions(user):
	acts = user.get_fight_actions()

	if user.gold >= 1000:
		acts = [ locale_manager.get('rooms.vietnam.missions_lepricone.first.phrase_3')] + acts

	return acts

def action(user, reply, text):
	if text == locale_manager.get('rooms.vietnam.missions_lepricone.first.phrase_4')and user.gold >= 1000:
		user.gold -= 1000
		user.leave(reply)
	else:
		user.fight_action(reply, text)
