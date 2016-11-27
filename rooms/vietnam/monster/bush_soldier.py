from localizations import locale_manager
name = locale_manager.get('rooms.vietnam.monster.bush_soldier.phrase_1')
hp = 280
damage_range = (20, 35)

coins = 200

loot = [ 'm-16' ]

def enter(user, reply):
	reply(locale_manager.get('rooms.vietnam.monster.bush_soldier.phrase_2'), photo='BQADAgADDgkAAmrZzgf0VttBNllKWwI')
	user.make_damage(0, 30, reply, name=locale_manager.get('rooms.vietnam.monster.bush_soldier.phrase_3'))
