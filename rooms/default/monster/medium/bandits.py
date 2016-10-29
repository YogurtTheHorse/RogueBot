import random

name = 'Группа Бандитов'

hp = 400

damage_range = ( 30, 60 )
loot = [ ]
coins = 300

actions = [ 'Да, есть', 'Нет', 'Блин, вы либо дольше держите, либо глубже опускайте!']

PHRASES = [
	'А нууу чики-брики и в дамки!', 'Сбоку, сбоку заходи!', 
	'Сышишь, фраер, ща ты у нас крякнешь!', 'Нука помааацаем, чтооо у нас тут', 
	'Я маслину словил!', 'Берём его тепленького!', 'Щаа мы вам, армбы недоделанные!'
]

def get_actions(user):
	if not user.get_room_temp('fight', False):
		return actions
	else:
		return user.get_fight_actions()

def action(user, reply, text):
	if not user.get_room_temp('fight', False):
		if text == actions[2]:
			reply('Бандиты расстроились, сказали «Ну ты плесень, ты б еще про Штирлица рассказал» и ушли.')
			user.leave(reply)
		else:
			reply('Бандиты достали оружие и атакуют вас, крича "Маачи казла!"')
			user.set_room_temp('fight', True)
	else:
		user.fight_action(reply, text)

def enter(user, reply):
	reply('Вы видите группу людей в плащах и капюшонах.')
	reply('Они вас заметили и говорят «Опа, фраерок нарисовался! Бабло, артефакты есть?»', photo='BQADAgADBwkAAmrZzgeViVze6T4hnAI')

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