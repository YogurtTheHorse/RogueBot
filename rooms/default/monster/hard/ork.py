from localizations import locale_manager
name = locale_manager.get('rooms.default.monster_hard.ork.phrase_2')
hp = 130
damage_range = ( 20, 40 )

coins = 150

loot = [ 'tooth' ]

def enter(user, reply):
	reply(
		locale_manager.get('rooms.default.monster_hard.ork.phrase_1'))
