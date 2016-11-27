from localizations import locale_manager
import random

name = locale_manager.get('rooms.default.boss.lich_king.phrase_1')

hp = 325000
damage_range = ( 80, 160 )

coins = random.randrange( 1000, 141000, 1)


def skill_preparing(user, reply, boss):
	reply(locale_manager.get('rooms.default.boss.lich_king.phrase_2'))
	