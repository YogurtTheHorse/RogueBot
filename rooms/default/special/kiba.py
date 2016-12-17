from localizations import locale_manager
import random
import usermanager
from constants import *

name = locale_manager.get('rooms.default.special.kiba.phrase_9')

STICKER_ENTER = 'BQADAgADbAADR_sJDEi39QLBEBigAg'
STICKER_ASKHELP = 'BQADAgADfgADR_sJDGLtdHnAJZ0uAg'
STICKER_FORGOT = 'BQADAgADlwADR_sJDPezoGBvDAf8Ag'
STICKER_CRASH = 'BQADAgADdgADR_sJDCyXvg1oAaN3Ag'
STICKER_SLEEP = 'BQADAgADlQADR_sJDIDpM6VA03zwAg'
STICKER_WHO_ARE_YOU = 'BQADAgADlwADR_sJDPezoGBvDAf8Ag'
STICKER_HIDDING = 'BQADAgADYAADR_sJDMcKS6xl6CpAAg'
STICKER_UNCERTAIN = 'BQADAgADkwADR_sJDJ5FA78SkL5OAg'
STICKER_GOOD_POTION = 'BQADAgADggADR_sJDGGwawbbnxyIAg'
STICKER_WONDER = 'BQADAgADZAADR_sJDBlEjbjLhUyVAg'

actions_enter = [ 'Привет キバ！', locale_manager.get('rooms.default.special.kiba.phrase_10'), locale_manager.get('rooms.default.special.kiba.phrase_11'), locale_manager.get('rooms.default.special.kiba.phrase_12'), locale_manager.get('rooms.default.special.kiba.phrase_13') ]
actions_fox_01 = [ locale_manager.get('rooms.default.special.kiba.phrase_14'), locale_manager.get('rooms.default.special.kiba.phrase_15') ]
actions_fox_02 = [ locale_manager.get('rooms.default.special.kiba.phrase_16'), locale_manager.get('rooms.default.special.kiba.phrase_17') ]
actions_chat = [ locale_manager.get('rooms.default.special.kiba.phrase_18'), locale_manager.get('rooms.default.special.kiba.phrase_19'), locale_manager.get('rooms.default.special.kiba.phrase_20') ]
actions_ask_help = [ locale_manager.get('rooms.default.special.kiba.phrase_21'), locale_manager.get('rooms.default.special.kiba.phrase_22') ]
actions_make_potion = [ locale_manager.get('rooms.default.special.kiba.phrase_23'), locale_manager.get('rooms.default.special.kiba.phrase_24') ]
actions_open_eye = [ locale_manager.get('rooms.default.special.kiba.phrase_25') ]
actions_drink = [ locale_manager.get('rooms.default.special.kiba.phrase_26'), locale_manager.get('rooms.default.special.kiba.phrase_27') ]

HAVE_NOTHING = locale_manager.get('rooms.default.special.kiba.phrase_28')
GIVE_ITEM = locale_manager.get('rooms.default.special.kiba.phrase_29')

FOX_COSTS = 10000

def actions_add_item(user): 
	actions = [
		HAVE_NOTHING
	]

	for i in user.get_items():
		if i.fightable:
			act = GIVE_ITEM + i.name
			if act not in actions:
				actions.append(act)

	return actions


## INITIALIZE

def enter(user, reply):
	msg = (
		locale_manager.get('rooms.default.special.kiba.phrase_1')'*キバ*!'
	)

	msg = msg + (
		locale_manager.get('rooms.default.special.kiba.phrase_2'))

	reply(msg, photo=STICKER_ENTER)

	user.set_room_temp('question', 'enter')


def get_actions(user):
	question = user.get_room_temp('question', def_val='enter')

	switcher = {
		'enter': actions_enter,
		'fox_01': actions_fox_01,
		'fox_02': actions_fox_02,
		'chat': actions_chat,
		'ask_help': actions_ask_help,
		'give_ingredient': actions_add_item,
		'give_stir': actions_add_item,
		'make_potion': actions_make_potion,
		'make_potion_success': actions_open_eye,
		'make_potion_failed': actions_open_eye,
		'drink': actions_drink
	}

	actions = switcher.get(question)

	if callable(actions):
		actions = actions(user)

	if question == 'enter':
		if not user.has_tag('know_kiba'):
			actions = filter(lambda q: q not in [ actions_enter[0], actions_enter[1] ], actions)

		if not user.has_tag('fox_payed'):
			actions = filter(lambda q: q is not actions_enter[2], actions)

		if user.has_tag('fox_payed'):
			actions = filter(lambda q: q is not actions_enter[1], actions)

	if question == 'fox_02':
		if user.gold < FOX_COSTS:
			actions = filter(lambda q: q is not actions_fox_02[0], actions)

	return actions


def action(user, reply, text):
	question = user.get_room_temp('question', def_val='enter')

	switcher = {
		'enter': action_enter,
		'fox_01': action_fox_01,
		'fox_02': action_fox_02,
		'chat': action_chat,
		'ask_help': action_ask_help,
		'give_ingredient': action_give_ingredient,
		'give_stir': action_give_stir,
		'make_potion': action_make_potion,
		'make_potion_success': action_make_potion_success,
		'make_potion_failed': action_make_potion_failed,
		'drink': action_drink
	}

	func = switcher.get(question)

	result = func(user, reply, text)

	if result is False or result is None:
		msg = (
			locale_manager.get('rooms.default.special.kiba.phrase_30')
		)

		reply(msg)


## ACTIONS

def action_enter(user, reply, text):
	if text == actions_enter[3]:
		msg = (
			locale_manager.get('rooms.default.special.kiba.phrase_31')
		)

		user.set_room_temp('question', 'chat')

		reply(msg, photo=STICKER_WHO_ARE_YOU)

		return True

	if text == actions_enter[0]:
		msg = (
			locale_manager.get('rooms.default.special.kiba.phrase_3'))

		user.set_room_temp('question', 'ask_help')

		reply(msg, photo=STICKER_ASKHELP)

		return True

	if text == actions_enter[1]:
		msg = (
			locale_manager.get('rooms.default.special.kiba.phrase_32')
		)

		user.set_room_temp('question', 'fox_01')

		reply(msg, photo=STICKER_WONDER)

		return True

	if text == actions_enter[2]:
		msg = (
			locale_manager.get('rooms.default.special.kiba.phrase_4'))

		user.remove_tag('fox_payed')

		reply(msg, photo=STICKER_SLEEP)

		user.new_pet(reply, 'fox')

		return True

	if text == actions_enter[4]:
		msg = locale_manager.get('rooms.default.special.kiba.phrase_5')

		reply(msg, photo=STICKER_SLEEP)

		user.leave(reply)

		return True


def action_fox_01(user, reply, text):
	if text == actions_fox_01[0]:
		msg = (
			locale_manager.get('rooms.default.special.kiba.phrase_6'))

		reply(msg.format(FOX_COSTS), photo=STICKER_FORGOT)

		user.set_room_temp('question', 'fox_02')

		return True

	if text == actions_fox_01[1]:
		msg = (
			locale_manager.get('rooms.default.special.kiba.phrase_7'))

		reply(msg, photo=STICKER_SLEEP)

		user.leave(reply)

		return True


def action_fox_02(user, reply, text):
	if text == actions_fox_02[0]:
		if user.paid(FOX_COSTS):
			msg = (
				locale_manager.get('rooms.default.special.kiba.phrase_33')
			)

			user.add_tag('fox_payed')

			reply(msg, photo=STICKER_SLEEP)

			user.leave(reply)

			return True

	if text == actions_fox_02[1]:
		msg = (
			locale_manager.get('rooms.default.special.kiba.phrase_8'))

		reply(msg, photo=STICKER_SLEEP)

		user.leave(reply)

		return True


def action_chat(user, reply, text):
	if not user.has_tag('know_kiba'):
		user.add_tag('know_kiba')

	if text == actions_chat[0]:
		msg = (
			'Ну как в каком? В чате бота конечно же, вот он @rogbotgroup.\n'
			locale_manager.get('rooms.default.special.kiba.phrase_34')
			locale_manager.get('rooms.default.special.kiba.phrase_35')
		)

		reply(msg, photo=STICKER_SLEEP)

		user.leave(reply)

		return True

	if text == actions_chat[1]:
		msg = (
			locale_manager.get('rooms.default.special.kiba.phrase_36')
			locale_manager.get('rooms.default.special.kiba.phrase_37')
			locale_manager.get('rooms.default.special.kiba.phrase_38')
		)

		reply(msg, photo=STICKER_SLEEP)

		user.leave(reply)

		return True

	if text == actions_chat[2]:
		msg = (
			'Когда ты уходил, на секунду тебе показалось, что キバ расстроился.\n'
			locale_manager.get('rooms.default.special.kiba.phrase_39')
			locale_manager.get('rooms.default.special.kiba.phrase_40')
		)

		reply(msg, photo=STICKER_SLEEP)

		user.leave(reply)

		return True


def action_ask_help(user, reply, text):
	if text == actions_ask_help[0]:
		msg = (
			locale_manager.get('rooms.default.special.kiba.phrase_41')
			locale_manager.get('rooms.default.special.kiba.phrase_42')
			locale_manager.get('rooms.default.special.kiba.phrase_43')
		)

		reply(msg, photo=STICKER_FORGOT)

		user.set_room_temp('question', 'give_ingredient')

		return True

	if text == actions_ask_help[1]:
		msg = (
			locale_manager.get('rooms.default.special.kiba.phrase_44')
			locale_manager.get('rooms.default.special.kiba.phrase_45')
		)

		reply(msg, photo=STICKER_SLEEP)

		user.leave(reply)

		return True


def action_give_ingredient(user, reply, text):
	if text == HAVE_NOTHING:
		msg = (
			locale_manager.get('rooms.default.special.kiba.phrase_46')
			locale_manager.get('rooms.default.special.kiba.phrase_47')
		)

		reply(msg, photo=STICKER_SLEEP)

		user.leave(reply)

		return True

	item_name = text.replace(GIVE_ITEM, '')

	item = user.get_item_by_name(item_name)

	if item is None:

		return False

	msg = (
		locale_manager.get('rooms.default.special.kiba.phrase_48')
	)

	reply(msg.format(item_name), photo=STICKER_FORGOT)

	user.remove_item(item.code_name)

	user.set_room_temp('ingredient', item.code_name)
	user.set_room_temp('question', 'give_stir')

	return True


def action_give_stir(user, reply, text):
	if text == HAVE_NOTHING:
		msg = (
			locale_manager.get('rooms.default.special.kiba.phrase_49')
			locale_manager.get('rooms.default.special.kiba.phrase_50')
		)

		reply(msg, photo=STICKER_SLEEP)

		user.leave(reply)

		return True

	item_name = text.replace(GIVE_ITEM, '')

	item = user.get_item_by_name(item_name)

	if item is None:

		return False

	msg = (
		locale_manager.get('rooms.default.special.kiba.phrase_51')
	)

	reply(msg.format(item_name), photo=STICKER_HIDDING)

	user.remove_item(item.code_name)

	user.set_room_temp('stir', item.code_name)
	user.set_room_temp('question', 'make_potion')

	return True


def action_make_potion(user, reply, text):
	if text == actions_make_potion[0]:
		msg = (
			locale_manager.get('rooms.default.special.kiba.phrase_52')
		)

		reply(msg)

		ingredient = user.get_room_temp('ingredient')
		stir = user.get_room_temp('stir')

		if ingredient == 'apple':
			user.set_room_temp('potion', 'success')

			if stir in ['good_spoon', 'spoon', 'fork'] or random.random() < 0.75:
				user.set_room_temp('question', 'make_potion_success')

			else:
				user.set_room_temp('question', 'make_potion_failed')

		else:
			user.set_room_temp('potion', 'failed')

			if random.random() < 0.25:
				user.set_room_temp('question', 'make_potion_success')

			else:
				user.set_room_temp('question', 'make_potion_failed')

		return True

	if text == actions_make_potion[1]:
		msg = (
			locale_manager.get('rooms.default.special.kiba.phrase_53')
			locale_manager.get('rooms.default.special.kiba.phrase_54')
		)

		reply(msg, photo=STICKER_SLEEP)

		user.leave(reply)

		return True


def action_make_potion_success(user, reply, text):
	if user.get_room_temp('potion') == 'success':
		msg = (
			locale_manager.get('rooms.default.special.kiba.phrase_55')
			locale_manager.get('rooms.default.special.kiba.phrase_56')
		)

		reply(msg, photo=STICKER_GOOD_POTION)

	else:
		msg = (
			locale_manager.get('rooms.default.special.kiba.phrase_57')
			locale_manager.get('rooms.default.special.kiba.phrase_58')
		)    

		reply(msg, photo=STICKER_UNCERTAIN)

	user.set_room_temp('question', 'drink')

	return True


def action_make_potion_failed(user, reply, text):
	msg = (
		locale_manager.get('rooms.default.special.kiba.phrase_59')
		locale_manager.get('rooms.default.special.kiba.phrase_60')
	)

	reply(msg, photo=STICKER_CRASH)

	user.set_room_temp('question', 'drink')

	return True


def action_drink(user, reply, text):
	if text == actions_drink[0]:
		if user.get_room_temp('potion') == 'success':
			msg = (
				locale_manager.get('rooms.default.special.kiba.phrase_61')
				locale_manager.get('rooms.default.special.kiba.phrase_62')
				locale_manager.get('rooms.default.special.kiba.phrase_63')
			)

			reply(msg, photo=STICKER_SLEEP)

			user.max_mp += 10

			user.leave(reply)

			return True

		else:
			msg = (
				locale_manager.get('rooms.default.special.kiba.phrase_64')
				locale_manager.get('rooms.default.special.kiba.phrase_65')
			)

			reply(msg, photo=STICKER_FORGOT)

			user.make_damage(10, 50, reply, death=False, defence=False)

			user.max_hp -= random.randrange(1, 10, 1)

			if user.max_hp < 10:
				user.max_hp = 10

			user.leave(reply)

			return True

	if text == actions_drink[1]:
		msg = (
			' — Ну не выливать же драгоценное зелье, — сказал キバ, выпил его и уснул.\n'
			locale_manager.get('rooms.default.special.kiba.phrase_66')
		)

		reply(msg, photo=STICKER_SLEEP)

		user.leave(reply)

		return True
