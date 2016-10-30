import random

name = 'Дети'

hp = 1000

damage_range = ( 70, 100 )
loot = [ ]
coins = 0

def get_actions(user):
	if not user.get_room_temp('fight', False):
		return ['Сладость', 'Гадость']
	else:
		return user.get_fight_actions()

def action(user, reply, text):
	if not user.get_room_temp('fight', False):
		if text == 'Сладость':
			if user.has_item('candy'):
				reply('Ты уже было протянул им конфету, но тебе заехали по лицу и украли у тебя все твои деньги')
				user.gold = 0
				user.leave(reply)
			else:
				reply('У тебя не оказалось сладостей, придется сбегать, хотя, что могут сде.. У НИХ ПИСТОЛЕТ. ЧЕРТОВЫ АМЕРИКАНЦЫ.')
				user.throw_dice(reply)
		else:
			reply('Ну что же ты детям гадость, а?\nБох накажет!')

			reply('Из неба сверкнула молния и все те святые, которых вспоминают на Хеллуин бог направил на тебя')
			user.set_room_temp('fight', True)
	else:
		user.fight_action(reply, text)

def enter(user, reply):
	reply('Вы видите группу людей в странных костюмах. Это мешок из макдака на голове?..')
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
		reply('Денег у святых нет. Негоже.')
		user.won(reply)
	else:
		user.set_room_temp('hp', hp)