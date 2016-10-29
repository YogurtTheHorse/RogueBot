from constants import *

name = 'Библиотека'

room_type = 'other'

def get_actions(user):
	return [ 'Кинуть кость и показать', 'Поучиться', 'Сказать своё имя' ]

def enter(user, reply):
	reply('На входе тебя встречает Библиотекарь.\nЛица не видно, но голос кажется смутно знакомым.\n\nПокажи, о путник, насколько ты умён!', photo='BQADAgAD4QgAAmrZzgf86MI3ztAEQwI')

def action(user, reply, text):
	actions = get_actions(user)

	if text == actions[0]:
		user.throw_dice(reply, 'derp')
	elif text == actions[1]:
		user.mana_damage += 5
		reply('Теперь ты умнее, но это стоило денег.')
		if not user.paid(50):
			reply('Библиотерю не понравилось, что ты попытался читать книги бесплатно.\nТы услышал тихий свист.\nЭто книга прилетела тебе в голову.')
			user.make_damage(40, 60, reply, name=name)
		user.leave(reply)
	else:
		if user.has_item('necromicrone'):
			usr_name = user.name.lower()
			user.leave(reply)
			reply('{0}? Хм-м-м...\nВ книге посетителей такого имени нет...\nВ этот момент Библиотекарь замечает у вас в руках Некрономикон.\n...\nУбирайся отсюда! Здесь не место для таких как ты!'.format(usr_name))
		else:
			usr_name = user.name.lower()
			if ('задрот' in usr_name) or ('book worm' in usr_name) or ('дракон' in usr_name):
				reply('Так-так, В списке вы есть. Но боюсь что ваш абонемент кончился, приходите в другой раз.')
				user.leave(reply)
			else:
				reply('{0}? Секунду.\nК сожалению в списке постоянных посетителей такого имени нет.\nИтак, насколько же ты умён?' .format(usr_name))


def dice(user, reply, result, subject='derp'):
	if result > DICE_MIDDLE:
		reply('Низковат ваш интеллект, однако.\nНо хоть системный блок и компьютер не путаете.\nИди отсюда быстрее, говорят глупость заразна.')
		user.leave(reply)
	else:
		reply('Дверь там.\nЧто такое дверь?\nТакой кусок дерева с ручкой, её обычно открывают.')
		user.leave(reply)
