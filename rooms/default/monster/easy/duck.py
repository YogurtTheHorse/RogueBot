from localizations import locale_manager
name = locale_manager.get('rooms.default.monster_easy.duck.phrase_1')

hp = 10
damage_range =  ( 5, 7 )

coins = 17

loot = [ ]

def enter(user, reply):
	reply(locale_manager.get('rooms.default.monster_easy.duck.phrase_2'))
