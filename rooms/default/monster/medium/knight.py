from localizations import locale_manager
import random

name = locale_manager.get('rooms.default.monster_medium.knight.phrase_1')

hp = 170
damage_range =  ( 30, 40 )

coins = 170

loot = [ random.choice(['shield', 'knight_helmet', 'knight_sword', 'knight_knee']) ]

def enter(user, reply):
	reply(locale_manager.get('rooms.default.monster_medium.knight.phrase_2'), photo='BQADAgAD-ggAAmrZzgdlwyeLQ-iTfwI')

	if user.rooms_count < 100:
		reply(locale_manager.get('rooms.default.monster_medium.knight.phrase_3'))
		user.leave(reply)

def make_damage(user, reply, dmg):
	hp = user.get_room_temp('hp', 0)
	hp -= max(0, dmg - 10)

	if hp <= 0:
		user.won(reply)
	else:
		user.set_room_temp('hp', hp)