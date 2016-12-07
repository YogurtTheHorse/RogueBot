from localizations import locale_manager
name = locale_manager.get('rooms.default.monster_medium.internet_troll.phrase_1')
damage_range = ( 10, 20 )
coins = 30
hp = 100

def enter(user, reply):
	reply(locale_manager.get('rooms.default.monster_medium.internet_troll.phrase_2'), photo='BQADAgADxwgAAmrZzgfaE3eq1S3hCwI')