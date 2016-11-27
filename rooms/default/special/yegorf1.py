from localizations import locale_manager
import random

name = locale_manager.get('rooms.default.special.yegorf1.phrase_7')

STICKER_YEGORF1 = 'BQADAgADQwADDLXzAxNNjVnoJZqxAg'

actions_enter = [ locale_manager.get('rooms.default.special.yegorf1.phrase_8') ]
actions_corridor = [ locale_manager.get('rooms.default.special.yegorf1.phrase_9'), 'Открыть дверь #445', 'Открыть дверь #444', 'Открыть дверь #443', 'Открыть дверь #442', 'Открыть дверь #441' ]
actions_choose_door_01 = [ locale_manager.get('rooms.default.special.yegorf1.phrase_10'), locale_manager.get('rooms.default.special.yegorf1.phrase_11') ]
actions_choose_door_02 = [ locale_manager.get('rooms.default.special.yegorf1.phrase_12'), locale_manager.get('rooms.default.special.yegorf1.phrase_13') ]
actions_choose_door_03 = [ locale_manager.get('rooms.default.special.yegorf1.phrase_14'), locale_manager.get('rooms.default.special.yegorf1.phrase_15') ]
actions_choose_door_04 = [ 'Зайти в дверь #308', 'Зайти в дверь #402', 'Зайти в дверь #253', 'Зайти в дверь #620', 'Зайти в дверь #636', 'Зайти в дверь #564' ]
actions_pray = [ locale_manager.get('rooms.default.special.yegorf1.phrase_16'), locale_manager.get('rooms.default.special.yegorf1.phrase_17'), locale_manager.get('rooms.default.special.yegorf1.phrase_18'), locale_manager.get('rooms.default.special.yegorf1.phrase_19'), locale_manager.get('rooms.default.special.yegorf1.phrase_20'), locale_manager.get('rooms.default.special.yegorf1.phrase_21'), locale_manager.get('rooms.default.special.yegorf1.phrase_22') ]

def doors_filter(user, doors):
	doors_filtered = filter(lambda room: user.get_room_temp(room, def_val='not-opened') == 'not-opened', doors)

	return doors_filtered

## INITIALIZE

def enter(user, reply):
	msg = (locale_manager.get('rooms.default.special.yegorf1.phrase_1'))

	reply(msg)

	user.set_room_temp('repeat_msg', locale_manager.get('rooms.default.special.yegorf1.phrase_23'))
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
			locale_manager.get('rooms.default.special.yegorf1.phrase_2'))

		reply(msg)

		user.set_room_temp('repeat_msg', locale_manager.get('rooms.default.special.yegorf1.phrase_24'))
		user.set_room_temp('question', 'corridor')

		return True


def action_corridor(user, reply, text):
	if text == actions_corridor[0]:
		msg = (
			locale_manager.get('rooms.default.special.yegorf1.phrase_3'))

		reply(msg)

		user.set_room_temp('repeat_msg', locale_manager.get('rooms.default.special.yegorf1.phrase_25'))
		user.set_room_temp('question', 'choose_door_01')

		return True

	if text in actions_corridor and user.get_room_temp(text, def_val='not-opened') == 'not-opened':
		msg = (
			locale_manager.get('rooms.default.special.yegorf1.phrase_26')
		)

		reply(msg)

		user.set_room_temp(text, 'opened')

		doors = actions_corridor[1:]

		opened_all_doors = all(user.get_room_temp(door, def_val='not-opened') == 'opened' for door in doors)

		if opened_all_doors and not user.get_room_temp('opened:corridor', def_val=False):
			user.set_room_temp('opened:corridor', True)

		if user.get_room_temp('opened:corridor', def_val=False):
			msg = (
				locale_manager.get('rooms.default.special.yegorf1.phrase_27')
			)

			reply(msg)

		return False


def action_choose_door_01(user, reply, text):
	if text == actions_choose_door_01[0]:
		msg = (
			locale_manager.get('rooms.default.special.yegorf1.phrase_28')
		)

		reply(msg)

		user.leave(reply)

		return True

	if text == actions_choose_door_01[1]:
		msg = (
			locale_manager.get('rooms.default.special.yegorf1.phrase_4'))

		reply(msg)

		user.set_room_temp('repeat_msg', locale_manager.get('rooms.default.special.yegorf1.phrase_29'))
		user.set_room_temp('question', 'choose_door_02')

		return True


def action_choose_door_02(user, reply, text):
	if text == actions_choose_door_02[0]:
		msg = (
			locale_manager.get('rooms.default.special.yegorf1.phrase_30')
		)

		reply(msg)

		user.set_room_temp('repeat_msg', locale_manager.get('rooms.default.special.yegorf1.phrase_31'))
		user.set_room_temp('question', 'choose_door_03')

		return True

	if text == actions_choose_door_02[1]:
		msg = (
			locale_manager.get('rooms.default.special.yegorf1.phrase_5'))

		reply(msg)

		user.set_room_temp(text, 'opened')

		return False


def action_choose_door_03(user, reply, text):
		if text == actions_choose_door_03[0]:
			msg = (
				locale_manager.get('rooms.default.special.yegorf1.phrase_32')
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
			locale_manager.get('rooms.default.special.yegorf1.phrase_33')
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
			locale_manager.get('rooms.default.special.yegorf1.phrase_6')
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
		user.death(reply, reason=locale_manager.get('rooms.default.special.yegorf1.phrase_34'))

		return True

