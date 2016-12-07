from localizations import locale_manager
name = locale_manager.get('rooms.default.monster_easy.archemage.phrase_1')

hp = 50
damage_range =  ( 15, 20 )

coins = 3

loot = [ 'mage_amulet' ]

def enter(user, reply):
	reply(locale_manager.get('rooms.default.monster_easy.archemage.phrase_2'), photo='AgAAmrZzgeKMJZP9j5DpQI')
