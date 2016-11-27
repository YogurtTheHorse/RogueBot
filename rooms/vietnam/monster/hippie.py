from localizations import locale_manager
name = locale_manager.get('rooms.vietnam.monster.hippie.phrase_1')

hp = 200
damage_range = (40, 50)

coins = 27

loot = [ 'vietnam_star' ]

def enter(user, reply):
    reply(locale_manager.get('rooms.vietnam.monster.hippie.phrase_2'))
