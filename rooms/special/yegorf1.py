import random

name = 'Человек'

STICKER_YEGORF1 = 'BQADAgADQwADDLXzAxNNjVnoJZqxAg'

actions_enter = [ 'Зайти в дверь' ]
actions_corridor = [ 'Идти дальше по коридору', 'Открыть дверь #445', 'Открыть дверь #444', 'Открыть дверь #443', 'Открыть дверь #442', 'Открыть дверь #441' ]
actions_choose_door_01 = [ 'Зайти в дверь слева', 'Зайти в дверь справа' ]
actions_choose_door_02 = [ 'Зайти в эту дверь', 'Постоять' ]
actions_choose_door_03 = [ 'Зайти в дверь синего цвета', 'Зайти в дверь красного цвета' ]
actions_choose_door_04 = [ 'Зайти в дверь #308', 'Зайти в дверь #402', 'Зайти в дверь #253', 'Зайти в дверь #620', 'Зайти в дверь #636', 'Зайти в дверь #564' ]
actions_pray = [ 'Молить рассказчика о выходе', 'Постоять', 'Сесть', 'Посидеть', 'Лечь', 'Полежать', 'Молить рассказчика о смерти' ]

def doors_filter(user, doors):
	doors_filtered = filter(lambda room: user.get_room_temp(room, def_val='not-opened') == 'not-opened', doors)

	return doors_filtered

## INITIALIZE

def enter(user, reply):
	msg = (
		'На мгновение тебя ослепило яркой вспышкой, и ты очень удивился тому, что никого кроме тебя в комнате не было.\n'
		'Перед тобой была открыта дверь, ведущая в коридор, и ты зашел в нее.'
	)

	reply(msg)

	user.set_room_temp('repeat_msg', 'Ты зашел в дверь перед собой.')
	user.set_room_temp('question', 'enter')


def get_actions(user):
	question = user.get_room_temp('question', def_val='enter')

	switcher = {
		'enter': actions_enter,
		'corridor': actions_corridor,
		'choose_door_01': actions_choose_door_01,
		'choose_door_02': actions_choose_door_02,
		'choose_door_03': actions_choose_door_03,
		'choose_door_04': actions_choose_door_04,
		'pray': actions_pray
	}

	actions = switcher.get(question)

	if callable(actions):
		actions = actions(user)

	actions = doors_filter(user, actions)

	return actions


def action(user, reply, text):
	question = user.get_room_temp('question', def_val='enter')

	switcher = {
		'enter': action_enter,
		'corridor': action_corridor,
		'choose_door_01': action_choose_door_01,
		'choose_door_02': action_choose_door_02,
		'choose_door_03': action_choose_door_03,
		'choose_door_04': action_choose_door_04,
		'pray': action_pray
	}

	func = switcher.get(question)

	result = func(user, reply, text)

	if result is False or result is None:
		msg = (
			user.get_room_temp('repeat_msg')
		)

		reply(msg)


## ACTIONS

def action_enter(user, reply, text):
	if text == actions_enter[0]:
		msg = (
			'Ты оказался в коридоре, но он не был обычным. На многих из дверей весели таблички с номерами.\n'
			'Но тебе стало интересно куда ведет этот коридор и пошел бальше.'
		)

		reply(msg)

		user.set_room_temp('repeat_msg', 'Ты пошел дальше по коридору.')
		user.set_room_temp('question', 'corridor')

		return True


def action_corridor(user, reply, text):
	if text == actions_corridor[0]:
		msg = (
			'В конце коридора была открытая дверь и ты зашел в нее.\n'
			'Перед тобой две открытых двери и ты зашел в дверь слева.'
		)

		reply(msg)

		user.set_room_temp('repeat_msg', 'Ты зашел в дверь слева.')
		user.set_room_temp('question', 'choose_door_01')

		return True

	if text in actions_corridor and user.get_room_temp(text, def_val='not-opened') == 'not-opened':
		msg = (
			'Эта дверь закрыта.'
		)

		reply(msg)

		user.set_room_temp(text, 'opened')

		doors = actions_corridor[1:]

		opened_all_doors = all(user.get_room_temp(door, def_val='not-opened') == 'opened' for door in doors)

		if opened_all_doors and not user.get_room_temp('opened:corridor', def_val=False):
			user.set_room_temp('opened:corridor', True)

		if user.get_room_temp('opened:corridor', def_val=False):
			msg = (
				'И правда, можно и дальше продолжать делать что вздумается, игнорируя подсказки.'
			)

			reply(msg)

		return False


def action_choose_door_01(user, reply, text):
	if text == actions_choose_door_01[0]:
		msg = (
			'Ты вышел в коридор.'
		)

		reply(msg)

		user.leave(reply)

		return True

	if text == actions_choose_door_01[1]:
		msg = (
			'Ты должен слушать подсказки и ненарушать их действий.\n'
			'Попробуем еще раз.\n\n'
			'Перед тобой одна открытая дверь и ты зашел в эту дверь.'
		)

		reply(msg)

		user.set_room_temp('repeat_msg', 'Ты зашел в эту дверь.')
		user.set_room_temp('question', 'choose_door_02')

		return True


def action_choose_door_02(user, reply, text):
	if text == actions_choose_door_02[0]:
		msg = (
			'Перед тобой две открытых дверей и ты зашел в дверь синего цвета.'
		)

		reply(msg)

		user.set_room_temp('repeat_msg', 'Ты зашел в дверь синего цвета.')
		user.set_room_temp('question', 'choose_door_03')

		return True

	if text == actions_choose_door_02[1]:
		msg = (
			'Ты должен слушать подсказки.\n'
			'И еще, я забираю у тебя этот вариант ответа.'
		)

		reply(msg)

		user.set_room_temp(text, 'opened')

		return False


def action_choose_door_03(user, reply, text):
		if text == actions_choose_door_03[0]:
			msg = (
				'Ты вышел в коридор.'
			)

			reply(msg)

			user.leave(reply)

			return True

		if text == actions_choose_door_03[1]:
			msg = (
				'*Нет!* Раз тебе не нужны подсказки, то дальше действуй сам!\n'
			)

			reply(msg)

			user.set_room_temp('repeat_msg', '')
			user.set_room_temp('question', 'choose_door_04')

			return False


def action_choose_door_04(user, reply, text):
	if text in actions_choose_door_04 and user.get_room_temp(text, def_val='not-opened') == 'not-opened':
		msg = (
			'Эта дверь закрыта'
		)

		reply(msg)

		user.set_room_temp(text, 'opened')

		doors = actions_choose_door_04

		opened_all_doors = all(user.get_room_temp(door, def_val='not-opened') == 'opened' for door in doors)

		if opened_all_doors and not user.get_room_temp('opened:choose_door_04', def_val=False):
			user.set_room_temp('opened:choose_door_04', True)

		if user.get_room_temp('opened:choose_door_04', def_val=False):
			user.set_room_temp(actions_pray[0], 'opened')
			user.set_room_temp(actions_pray[1], 'not-opened')
			user.set_room_temp(actions_pray[2], 'opened')
			user.set_room_temp(actions_pray[3], 'opened')
			user.set_room_temp(actions_pray[4], 'opened')
			user.set_room_temp(actions_pray[5], 'opened')
			user.set_room_temp(actions_pray[6], 'opened')
			user.set_room_temp('question', 'pray')

	return True


def action_pray(user, reply, text):
	if text == actions_pray[0]:
		msg = (
			'Что? Нужна помощь?\n'
			'На этот раз я тебя прощу, но впредь будь послушным.\n'
			'@yegorf1 ударил тебя тростью и ты вылетаешь в коридор через открывшуюся дверь.'
		)

		reply(msg, photo=STICKER_YEGORF1)

		user.make_damage(10, 50, reply, defence=False, death=False)

		user.leave(reply)

		return True

	if text == actions_pray[1]:
		stay_count = user.get_room_temp('stay', def_val=0)

		if stay_count > 3:
			user.set_room_temp(actions_pray[0], 'not-opened')
			user.set_room_temp(actions_pray[1], 'opened')
			user.set_room_temp(actions_pray[2], 'not-opened')

		user.set_room_temp('stay', stay_count + 1)

		return True

	if text == actions_pray[2]:
		user.set_room_temp(actions_pray[2], 'opened')
		user.set_room_temp(actions_pray[3], 'not-opened')

		return True

	if text == actions_pray[3]:
		user.set_room_temp(actions_pray[3], 'opened')
		user.set_room_temp(actions_pray[4], 'not-opened')

		return True

	if text == actions_pray[4]:
		user.set_room_temp(actions_pray[4], 'opened')
		user.set_room_temp(actions_pray[5], 'not-opened')

		return True

	if text == actions_pray[5]:
		user.set_room_temp(actions_pray[5], 'opened')
		user.set_room_temp(actions_pray[6], 'not-opened')

		return True

	if text == actions_pray[6]:
		user.death(reply, reason='По собственному желанию')

		return True

