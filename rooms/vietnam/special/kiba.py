import random
import usermanager
from constants import *

name = 'Человек'

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

actions_enter = [ 'Привет キバ！', 'Попросить лису', 'Ты привез мне лису?', 'Ты кто?', 'Уйти' ]
actions_fox_01 = [ 'Да, можно мне лису?', 'А.. нет, я оговорился' ]
actions_fox_02 = [ 'Хорошо, вот мои деньги', 'Слишком дорого' ]
actions_chat = [ 'Каком чате?', 'Ага, я понял кто ты', 'Уйти' ]
actions_ask_help = [ 'Конечно, чем тебе помочь?', 'Извини, но у меня нет времени.' ]
actions_make_potion = [ 'Размешать', 'Не размешавать' ]
actions_open_eye = [ 'Открыть глаза' ]
actions_drink = [ 'Выпить', 'Не пить' ]

HAVE_NOTHING = 'У меня ничего нет'
GIVE_ITEM = 'Дать '

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
		'На негнущихся коленях ты проходишь '
		'в середину комнаты. Да, глаза не подвели, это действительно...\n\n'
		'*キバ*!'
	)

	msg = msg + (
		'\n\n'
		'*Бууу!*'
	)

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
			'Я тебя не слышу!!! Прошу, говори громче.'
		)

		reply(msg)


## ACTIONS

def action_enter(user, reply, text):
	if text == actions_enter[3]:
		msg = (
			'*Опашки-опашки* Неужели ты меня не знаешь? Я часто бываю в чате.\n'
		)

		user.set_room_temp('question', 'chat')

		reply(msg, photo=STICKER_WHO_ARE_YOU)

		return True

	if text == actions_enter[0]:
		msg = (
			'И тебе привет!\n'
			'Ты ведь можешь помочь мне закончить зелье?\n'
			'Остался последний ингредиент, но я не знаю какой.'
		)

		user.set_room_temp('question', 'ask_help')

		reply(msg, photo=STICKER_ASKHELP)

		return True

	if text == actions_enter[1]:
		msg = (
			'*Лису?* Ты хочешь лису??'
		)

		user.set_room_temp('question', 'fox_01')

		reply(msg, photo=STICKER_WONDER)

		return True

	if text == actions_enter[2]:
		msg = (
			'Конечно, вот она!\n'
			'Заходи ко мне еще..'
		)

		user.remove_tag('fox_payed')

		reply(msg, photo=STICKER_SLEEP)

		user.new_pet(reply, 'fox')

		return True

	if text == actions_enter[4]:
		msg = (
			'Когда ты уходил, на секунду тебе показалось, что キバ расстроился.\n'
			'Ты обернулся и увидел, что он спит.\n'
			' — Вот же соня!, — подумал ты'
		)

		reply(msg, photo=STICKER_SLEEP)

		user.leave(reply)

		return True


def action_fox_01(user, reply, text):
	if text == actions_fox_01[0]:
		msg = (
			'Дай подумать..\n'
			'Думаю я мог бы достать одну лису, это будет стоить {} золотых.\n'
			'Что думаешь?'
		)

		reply(msg.format(FOX_COSTS), photo=STICKER_FORGOT)

		user.set_room_temp('question', 'fox_02')

		return True

	if text == actions_fox_01[1]:
		msg = (
			'Нет? Ну ладно. Я просто знаю где достать одну лису.\n'
			'Если понадобится, то заходи..'
		)

		reply(msg, photo=STICKER_SLEEP)

		user.leave(reply)

		return True


def action_fox_02(user, reply, text):
	if text == actions_fox_02[0]:
		if user.paid(FOX_COSTS):
			msg = (
				'Отлично! Заходи через неделю, я привезу лису.'
			)

			user.add_tag('fox_payed')

			reply(msg, photo=STICKER_SLEEP)

			user.leave(reply)

			return True

	if text == actions_fox_02[1]:
		msg = (
			'Нет? Ну ладно. Я просто знаю где достать одну лису.\n'
			'Если понадобится, то заходи..'
		)

		reply(msg, photo=STICKER_SLEEP)

		user.leave(reply)

		return True


def action_chat(user, reply, text):
	if not user.has_tag('know_kiba'):
		user.add_tag('know_kiba')

	if text == actions_chat[0]:
		msg = (
			'Ну как в каком? В чате бота конечно же, вот он @rogbotgroup.\n'
			'Если увидишь меня там, то передавай привет!\n'
			'А я спать.. потопа...'
		)

		reply(msg, photo=STICKER_SLEEP)

		user.leave(reply)

		return True

	if text == actions_chat[1]:
		msg = (
			'Очень хорошо, что ты знаешь меня, я правда очень рад!\n'
			'Если увидишь меня в чате, то передавай привет!\n'
			'А я спать.. потопа...'
		)

		reply(msg, photo=STICKER_SLEEP)

		user.leave(reply)

		return True

	if text == actions_chat[2]:
		msg = (
			'Когда ты уходил, на секунду тебе показалось, что キバ расстроился.\n'
			'Ты обернулся и увидел, что он спит.\n'
			' — Вот же соня!, — подумал ты'
		)

		reply(msg, photo=STICKER_SLEEP)

		user.leave(reply)

		return True


def action_ask_help(user, reply, text):
	if text == actions_ask_help[0]:
		msg = (
			'*Ура!* Смотри, вот мой котел. В нем я готовлю вкусное зелье.\n'
			'Но к сожалению я забыл последний ингредиент для него.\n'
			'У тебя есть идеи?'
		)

		reply(msg, photo=STICKER_FORGOT)

		user.set_room_temp('question', 'give_ingredient')

		return True

	if text == actions_ask_help[1]:
		msg = (
			'Эх, вот так всегда.. Но все равно я был очень рад тебя видеть!\n'
			'Заходи ко мне еще..'
		)

		reply(msg, photo=STICKER_SLEEP)

		user.leave(reply)

		return True


def action_give_ingredient(user, reply, text):
	if text == HAVE_NOTHING:
		msg = (
			'Эх, вот так всегда.. Но все равно я был очень рад тебя видеть!\n'
			'Заходи ко мне еще..'
		)

		reply(msg, photo=STICKER_SLEEP)

		user.leave(reply)

		return True

	item_name = text.replace(GIVE_ITEM, '')

	item = user.get_item_by_name(item_name)

	if item is None:

		return False

	msg = (
		'Отлично, кидай {} в котел и давай размешаем.. У тебя есть чем размешать?'
	)

	reply(msg.format(item_name), photo=STICKER_FORGOT)

	user.remove_item(item.code_name)

	user.set_room_temp('ingredient', item.code_name)
	user.set_room_temp('question', 'give_stir')

	return True


def action_give_stir(user, reply, text):
	if text == HAVE_NOTHING:
		msg = (
			'Эх, вот так всегда.. Но все равно я был очень рад тебя видеть!\n'
			'Заходи ко мне еще..'
		)

		reply(msg, photo=STICKER_SLEEP)

		user.leave(reply)

		return True

	item_name = text.replace(GIVE_ITEM, '')

	item = user.get_item_by_name(item_name)

	if item is None:

		return False

	msg = (
		'Твоя {}, ты и мешай!'
	)

	reply(msg.format(item_name), photo=STICKER_HIDDING)

	user.remove_item(item.code_name)

	user.set_room_temp('stir', item.code_name)
	user.set_room_temp('question', 'make_potion')

	return True


def action_make_potion(user, reply, text):
	if text == actions_make_potion[0]:
		msg = (
			'*ВЗРЫВ!*'
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
			'Я тоже не буду это мешать. Что же, придется вылить и готовить зелье заново.\n'
			'Но позже, я потопал.. спа...'
		)

		reply(msg, photo=STICKER_SLEEP)

		user.leave(reply)

		return True


def action_make_potion_success(user, reply, text):
	if user.get_room_temp('potion') == 'success':
		msg = (
			'*Ура!* Похоже у нас получилось сделать его.\n'
			'Вот то зелье, которое ты приготовил, будешь его пить?'
		)

		reply(msg, photo=STICKER_GOOD_POTION)

	else:
		msg = (
			'*Ура!* Похоже у нас получилось сделать его, хоть оно и немного другого цвета.\n'
			'Вот то зелье которое ты приготовил, будешь его пить?'
		)    

		reply(msg, photo=STICKER_UNCERTAIN)

	user.set_room_temp('question', 'drink')

	return True


def action_make_potion_failed(user, reply, text):
	msg = (
		'*Ох* Что же ты натворил? Мою лабараторию всю разнесло.\n'
		'Вот то зелье которое ты приготовил, будешь его пить?'
	)

	reply(msg, photo=STICKER_CRASH)

	user.set_room_temp('question', 'drink')

	return True


def action_drink(user, reply, text):
	if text == actions_drink[0]:
		if user.get_room_temp('potion') == 'success':
			msg = (
				'Похоже это было зелье маны! Твоя максимальная мана увеличена на 10!\n'
				'Я был очень рад тебя видеть!\n'
				'Заходи ко мне еще..'
			)

			reply(msg, photo=STICKER_SLEEP)

			user.max_mp += 10

			user.leave(reply)

			return True

		else:
			msg = (
				' — Да, это не то зелье. Я провожу тебя до коридора, а дальше как-нибудь сам, окей?\n\n'
				'Ты отравился и твое максимальное здоровье немного уменьшилось.'
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
			' — Вот же соня!, — подумал ты'
		)

		reply(msg, photo=STICKER_SLEEP)

		user.leave(reply)

		return True
