from localizations import locale_manager

name = locale_manager.get('rooms.default.monster_expert.saitama.name')

hp = 300000
damage_range = (3000, 4000 )

coin = 0

loot = [ ]

def enter(user, reply):
	reply(locale_manager.get('rooms.default.monster_expert.saitama.enter'))
		
