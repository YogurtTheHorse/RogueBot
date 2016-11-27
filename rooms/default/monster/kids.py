from localizations import locale_manager
import random

name = locale_manager.get('rooms.default.monster.kids.phrase_1')

hp = 1000

damage_range = ( 70, 100 )
loot = [ ]
coins = 0

def get_actions(user):
	if not user.get_room_temp('fight', False):
		return [locale_manager.get('rooms.default.monster.kids.phrase_2'), locale_manager.get('rooms.default.monster.kids.phrase_3')]
	else:
		return user.get_fight_actions()

def action(user, reply, text):
	if not user.get_room_temp('fight', False):
		if text == locale_manager.get('rooms.default.monster.kids.phrase_4'):
			if user.has_item('candy'):
				reply(locale_manager.get('rooms.default.monster.kids.phrase_5'))
				user.gold = 0
				user.leave(reply)
			else:
				reply(locale_manager.get('rooms.default.monster.kids.phrase_6'))
				user.throw_dice(reply)
		else:
			reply(locale_manager.get('rooms.default.monster.kids.phrase_7'))

			reply(locale_manager.get('rooms.default.monster.kids.phrase_8'))
			user.set_room_temp('fight', True)
	else:
		user.fight_action(reply, text)

def enter(user, reply):
	reply(locale_manager.get('rooms.default.monster.kids.phrase_9'))
	reply('Д̶е̶н̶ь̶г̶и̶ ̶и̶л̶и̶ ̶ж̶и̶з̶н̶ь̶Сладость или гадость?', photo='BQADAgAD6ggAAmrZzgfc2fdWTq6Q8AI')

	user.set_room_temp('fight', False)

def dice(user, reply, result, subject=None):
	reply('Не получилось :(\nНо зато пистолет стрелял конфетами!')

	for i in range(5):
		user.add_item('special', 'candy')

	user.leave(reply)

def make_damage(user, reply, dmg):
	hp = user.get_room_temp('hp', 0)
	hp -= max(1, dmg)

	if hp <= 0:
		reply(locale_manager.get('rooms.default.monster.kids.phrase_10'))
		user.won(reply)
	else:
		user.set_room_temp('hp', hp)