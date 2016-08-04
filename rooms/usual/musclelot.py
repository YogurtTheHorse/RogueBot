from constants import *

name = 'Спортзал'

room_type = 'other'

actions = [ 'Кинуть кость и показать', 'Сказать свое имя, чтобы знал, кто я', 'Подкачаться', 'Попробовать просто уйти' ]

def enter(user, reply):
	msg = (
		'На входе вас встречает Сэр Качколот!\n\n'
		'«Сколько качаешь?»'
	)
	reply(msg)

def action(user, reply, text):
	if text == actions[0]:
		user.throw_dice(reply, 'zhmesh')
	elif text == actions[1]:
		usr_name = user.name.lower()
		if ('качок' in usr_name) or ('качколот' in usr_name):
			reply('Другое дело, дай пять!')
			user.throw_dice(reply, 'five')
		else:
			reply('{0}? Мне это ничего не говорит.\nСколько качаешь?'.format(usr_name))
	elif text == actions[2]:
		user.defence += 1
		reply('Ты подкачался. Твоя сила выросла, но это стоило денег.')
		if not user.paid(50):
			msg = (
				'Качкам не понравилось, что ты пользовался их спортзалом без денег.\n'
				'То, что они тебя не выпускали, их не смущает. Тебя побили'
			)
			reply(msg)
			user.make_damage(40, 60)
		user.leave(reply)
	elif text == actions[3]:
		reply('Мускулистые качки окружили выход, у тебя ничего не вышло')

def dice(user, reply, result, subject='zhmesh'):
	if result > DICE_MIDDLE:
		if subject == 'zhmesh':
			reply('Это конечно немного, но я видел рыцарей и по хуже')
		else:
			reply('Ты отбил Сэру Качкалоту руку.\nКрасава!')

		reply('Ты уходишь с миром')
	else:
		if subject == 'zhmesh':
			reply('Слишком мало, поэтому пришлось подкачаться и ты устал')
			user.make_damage(5, 10)
		else:
			reply('Сэру Качкалот отбил тебе руку.\nКрасава!')
			user.make_damage(10, 20)
	user.leave(reply)
