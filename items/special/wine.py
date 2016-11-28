from localizations import locale_manager
import random

name = locale_manager.get('items.special.wine.phrase_2')

description = (
	locale_manager.get('items.special.wine.phrase_1'))

price = 300
fightable = True
disposable = True


def can_use(user, reply, room):
	reply(locale_manager.get('items.special.wine.phrase_3'))

	return random.random() > 0.3 and room.code_name != 'doctor_who' and room.room_type != 'boss'


def success(user, reply, room):
	reply(locale_manager.get('items.special.wine.phrase_4'))
	user.won(reply)


def failure(user, reply, room):
	reply(locale_manager.get('items.special.wine.phrase_5'))

	if room.room_type != 'boss':
		user.death(reply, reason=name)

	else:
		reply(locale_manager.get('items.special.wine.phrase_6'))
