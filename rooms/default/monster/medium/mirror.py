from localizations import locale_manager
from utils import costumes

from constants import *

name = locale_manager.get('rooms.default.monster_medium.mirror.phrase_1')

hp = 1
element = NONE
damage_range =  ( 0, 0 )

coins = 200

loot = [ ]

def enter(user, reply):
	msg = (
		locale_manager.get('rooms.default.monster_medium.mirror.phrase_2').format(costumes.get_costume(user.costume)['who'])
	)
	reply(msg, photo='BQADAgAD2ggAAmrZzgeHYxYQWFaEZgI')

	user.set_room_temp('hp', user.hp)

	ch = user.get_charisma()

	if ch < 0:
		reply(locale_manager.get('rooms.default.monster_medium.mirror.phrase_3'))
		user.won(reply)
	elif ch > 15:
		reply(locale_manager.get('rooms.default.monster_medium.mirror.phrase_6'))
		user.won(reply)

def make_damage(user, reply, dmg):
	hp = user.get_room_temp('hp', 0)
	hp -= dmg + 1

	if hp <= 0:
		user.won(reply)

		reply(locale_manager.get('rooms.default.monster_medium.mirror.phrase_4'))

		user.make_damage(0, -hp, reply, defence=False, name=name)
	else:
		user.set_room_temp('hp', hp)

		reply(locale_manager.get('rooms.default.monster_medium.mirror.phrase_5').format(dmg))
		user.make_damage(dmg, dmg, reply, defence=False, name=name)
