from localizations import locale_manager
name = locale_manager.get('rooms.default.monster_medium.ghoul.phrase_1')
hp = 10

damage_range = ( 15, 35 )
loot = [ ]

def enter(user, reply):
	reply(locale_manager.get('rooms.default.monster_medium.ghoul.phrase_2'))
