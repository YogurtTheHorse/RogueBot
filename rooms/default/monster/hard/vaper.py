from localizations import locale_manager
﻿name = locale_manager.get('rooms.default.monster_hard.vaper.phrase_1')
hp = 80
damage_range = ( 10, 20 )
loot = [ 'mechmod' ]

def enter(user, reply):
	reply(locale_manager.get('rooms.default.monster_hard.vaper.phrase_2'), photo='BQADAgAD1ggAAmrZzgenvIB-RsNAhwI')
