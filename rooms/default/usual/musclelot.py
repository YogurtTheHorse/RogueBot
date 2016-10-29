from constants import *

LASER_ESCAPE = 'tried_escape'

name = 'Спортзал'

room_type = 'other'

def get_actions(user):
	if user.has_tag(EVIL_MUSCLELOT):
		actions = [ 'Попробовать отбиться' ]
		if user.has_item('laser'):
			actions.append('Воспользоваться указкой еще раз')

		return actions
	else:
		if user.get_room_temp(LASER_ESCAPE, False):
			return [ 'Кинуть кость и показать', 'Сказать свое имя, чтобы знал, кто я', 'Подкачаться', 'Посветить указкой в глаза и сбежать' ]
		else:
			return [ 'Кинуть кость и показать', 'Сказать свое имя, чтобы знал, кто я', 'Подкачаться', 'Попробовать просто уйти' ]

def enter(user, reply):
	if user.has_tag(EVIL_MUSCLELOT):
		msg = (
			'На входе вас встречает Сэр Качколот!\n\n'
			'Он и его друзья помнят старые обиды.'
		)
		reply(msg)
	else:
		msg = (
			'На входе вас встречает Сэр Качколот!\n\n'
			'«Сколько качаешь?»'
		)
		reply(msg, photo='BQADAgAD1AgAAmrZzgcux0BHbF1X1gI')

def action(user, reply, text):
	if user.has_tag(EVIL_MUSCLELOT):
		evil_action(user, reply, text)
	else:
		normal_action(user, reply, text)

def evil_action(user, reply, text):
	actions = get_actions(user)

	if text == actions[0]:
		user.throw_dice(reply, 'fight')
	elif len(actions) > 1 and text == actions[1]:
		msg = (
			'Пока ты пытался снова отвлечь их, они просто подошли, избили тебя и украли деньги.\n'
			'Ты правда думал, что это сработает дважды?'
		)
		reply(msg)

		user.make_damage(30, 40, reply, name=name)
		user.steal(20)
		user.leave(reply)

def normal_action(user, reply, text):
	actions = get_actions(user)

	if text == actions[0]:
		user.throw_dice(reply, 'zhmesh')
	elif text == actions[1]:
		usr_name = user.name.lower()
		if ('качок' in usr_name) or ('качколот' in usr_name) or ('качкалот' in usr_name):
			reply('Другое дело, дай пять!')
			user.throw_dice(reply, 'five')
		else:
			reply('{0}? Мне это ничего не говорит.\nСколько качаешь?'.format(usr_name))
	elif text == actions[2]:
		user.damage += 5
		reply('Ты подкачался. Твоя сила выросла, но это стоило денег.')
		if not user.paid(50):
			msg = (
				'Качкам не понравилось, что ты пользовался их спортзалом без денег.\n'
				'То, что они тебя не выпускали, их не смущает. Тебя побили.'
			)
			reply(msg)
			user.make_damage(40, 60, reply, name=name)
		user.leave(reply)
	elif text == actions[3]:
		if user.get_room_temp(LASER_ESCAPE, False):
			reply('Ты ослепил качков лазерной указкой и убежал. Им это не очень понравилось.')
			user.escape(reply, True)
			user.add_tag(EVIL_MUSCLELOT)
		else:
			reply('Мускулистые качки окружили выход, у тебя ничего не вышло.')
			user.escape(reply, False)

			if user.has_item('laser'):
				user.set_room_temp(LASER_ESCAPE, True)

def dice(user, reply, result, subject='zhmesh'):
	if result > DICE_MIDDLE:
		if subject == 'zhmesh':
			reply('Это, конечно, не много, но я видел рыцарей и похуже.')
		elif subject == 'fight':
			reply('Тебя потрепали, но не смертельно. Все обошлось.')
			user.make_damage(5, 10, reply, False, name=name)
		else:
			reply('Ты отбил Сэру Качкалоту руку.\nКрасава!')

		reply('Ты уходишь с миром')
	else:
		if subject == 'zhmesh':
			reply('Слишком мало, поэтому пришлось подкачаться. Ты устал.')
			user.make_damage(5, 10, reply, name=name)
		elif subject == 'fight':
			reply('Тебя в очередной раз хорошенько избили. Не стоило светить в глаза.')
			user.make_damage(50, 60, reply, name=name)
		else:
			reply('Сэр Качкалот отбил тебе руку.\nКрасава!')
			user.make_damage(5, 10, reply, name=name)
	user.leave(reply)
