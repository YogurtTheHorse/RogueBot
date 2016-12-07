from localizations import locale_manager
name = locale_manager.get('rooms.default.monster_hard.jayson.phrase_1')
hp = 100

damage_range = ( 15, 30 )

coins = 50
loot = [ ]

def enter(user, reply):
    msg = locale_manager.get('rooms.default.monster_hard.jayson.phrase_2')
    reply(msg, photo='BQADAgAD8ggAAmrZzgew8H9_s6AtPAI')
