from localizations import locale_manager
import random

name = locale_manager.get('rooms.default.monster_medium.bandits.phrase_1')

hp = 400

damage_range = ( 30, 60 )
loot = [ ]
coins = 300

actions = [ locale_manager.get('rooms.default.monster_medium.bandits.phrase_2'), locale_manager.get('rooms.default.monster_medium.bandits.phrase_3'), locale_manager.get('rooms.default.monster_medium.bandits.phrase_4')]

PHRASES = [
	locale_manager.get('rooms.default.monster_medium.bandits.phrase_5'), locale_manager.get('rooms.default.monster_medium.bandits.phrase_6'), 
	locale_manager.get('rooms.default.monster_medium.bandits.phrase_7'), locale_manager.get('rooms.default.monster_medium.bandits.phrase_8'), 
	locale_manager.get('rooms.default.monster_medium.bandits.phrase_9'), locale_manager.get('rooms.default.monster_medium.bandits.phrase_10'), locale_manager.get('rooms.default.monster_medium.bandits.phrase_11')
]

def get_actions(user):
	if not user.get_room_temp('fight', False):
		return actions
	else:
		return user.get_fight_actions()

def action(user, reply, text):
	if not user.get_room_temp('fight', False):
		if text == actions[2]:
			reply(locale_manager.get('rooms.default.monster_medium.bandits.phrase_12'))
			user.leave(reply)
		else:
			reply('Бандиты достали оружие и атакуют вас, крича "Маачи казла!"')
			user.set_room_temp('fight', True)
	else:
		user.fight_action(reply, text)

def enter(user, reply):
	reply(locale_manager.get('rooms.default.monster_medium.bandits.phrase_13'))
	reply(locale_manager.get('rooms.default.monster_medium.bandits.phrase_14'), photo='BQADAgADBwkAAmrZzgeViVze6T4hnAI')

	user.set_room_temp('fight', False)

def dice(user, reply, result, subject=None):
	return user.fight_dice(reply, result, subject)

def make_damage(user, reply, dmg):
	hp = user.get_room_temp('hp', 0)
	hp -= max(1, dmg)

	if hp <= 0:
		user.won(reply)
	else:
		reply(random.choice(PHRASES))
		user.set_room_temp('hp', hp)