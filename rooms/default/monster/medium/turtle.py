from localizations import locale_manager
name = locale_manager.get('rooms.default.monster_medium.turtle.phrase_1')
hp = 200
damage_range = (10, 12)

loot = [ 'mechanic_shell' ]

def enter(user, reply):
	reply(locale_manager.get('rooms.default.monster_medium.turtle.phrase_2'), photo='BQADAgADCwkAAmrZzgca3p47J9mzpAI')

	if user.rooms_count < 35:
		reply(locale_manager.get('rooms.default.monster_medium.turtle.phrase_3'))
		user.leave(reply)