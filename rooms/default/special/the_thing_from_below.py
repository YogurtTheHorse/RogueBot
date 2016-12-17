from localizations import locale_manager
name = locale_manager.get('rooms.default.special.the_thing_from_below.phrase_1')

hp = 900
damage_range = ( 40, 80 )

coins = 900
loot = [ 'puzzle' ]
is_monster = True

def enter(user, reply):
	reply(locale_manager.get('rooms.default.special.the_thing_from_below.enter'))

	if user.rooms_count < 800:
		reply(locale_manager.get('rooms.default.special.the_thing_from_below.to_little'))
		user.leave(reply)
	else:
		reply(locale_manager.get('rooms.default.special.the_thing_from_below.evil'))

def get_actions(user):
	return user.get_fight_actions()

def action(user, reply, text):
	user.fight_action(reply, text)	