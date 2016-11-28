from localizations import locale_manager
import random

name = locale_manager.get('items.special.magic_scroll.phrase_3')

description = (
	locale_manager.get('items.special.magic_scroll.phrase_4')
)

mp_cost = 100

price = 300
fightable = True
disposable = True


def can_use(user, reply, room):
	return random.random() > 0.25 and room.code_name != 'doctor_who' and room.room_type != 'boss'


def fight_use(user, reply, room):
	if user.mp >= mp_cost:
		reply(locale_manager.get('items.special.magic_scroll.phrase_5'))
		user.mp -= mp_cost

	else:
		reply(locale_manager.get('items.special.magic_scroll.phrase_6'))

	return 0


def success(user, reply, room):
	reply(
		locale_manager.get('items.special.magic_scroll.phrase_1'))

	user.won(reply)


def failure(user, reply, room):
	if room.room_type != 'boss':
		reply(
			locale_manager.get('items.special.magic_scroll.phrase_2'))

		user.reborn(reply, locale_manager.get('items.special.magic_scroll.phrase_7'), name=locale_manager.get('items.special.magic_scroll.phrase_8'))

	else:
		reply(locale_manager.get('items.special.magic_scroll.phrase_9'))
	