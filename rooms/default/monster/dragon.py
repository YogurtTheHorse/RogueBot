from localizations import locale_manager
name = locale_manager.get('rooms.default.monster.dragon.phrase_1')

hp = 140
damage_range =  ( 15, 30 )

coins = 300

loot = [ 'dragon_sword' ]

def enter(user, reply):
	reply(locale_manager.get('rooms.default.monster.dragon.phrase_2'), photo='BQADAgADywgAAmrZzgeQZg8qNy8d0AI')

	if user.rooms_count < 50:
		reply(locale_manager.get('rooms.default.monster.dragon.phrase_3'))
		user.leave(reply)
