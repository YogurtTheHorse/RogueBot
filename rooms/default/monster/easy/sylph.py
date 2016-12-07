from localizations import locale_manager

name = locale_manager.get('rooms.default.monster_easy.sylph.phrase_1')
hp = 25
damage_range = (7, 14)

coins = 20

loot = ['ballet_tutu']  # Балетная пачка


def enter(user, reply):
	reply(locale_manager.get('rooms.default.monster_easy.sylph.phrase_2'), photo='BQADAgADDAkAAmrZzgdS6xec3MqmYQI')