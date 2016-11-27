from localizations import locale_manager
import random
from constants import *

READY = locale_manager.get('rooms.default.usual.rick_and_morty.phrase_1')
ESCAPE = locale_manager.get('rooms.default.usual.rick_and_morty.phrase_2')
HELLO = locale_manager.get('rooms.default.usual.rick_and_morty.phrase_3')
FIGHT = locale_manager.get('rooms.default.usual.rick_and_morty.phrase_4')

name = locale_manager.get('rooms.default.usual.rick_and_morty.phrase_5')

def enter(user, reply):
	msg = (
		locale_manager.get('rooms.default.usual.rick_and_morty.phrase_6'))
	reply(msg)
	user.set_room_temp('question', 'first')

def action(user, reply, text):
	question = user.get_room_temp('question', def_val='first')

	if question == 'first':
		if text == READY:
			reply('Ты подошел ближе, и к тебе вышли:\nКакой-то мужик в халате и с синими волосами и мальчуган лет 14 в желтой футболке.')
			user.set_room_temp('question', 'action')
		elif text == ESCAPE:
			reply(locale_manager.get('rooms.default.usual.rick_and_morty.phrase_7'))
			user.leave(reply)
	elif question == 'action':
		if text == HELLO:
			reply(locale_manager.get('rooms.default.usual.rick_and_morty.phrase_8'))
			reply(
				'—Рик, нам... нам надо отсюда убираться, Рик... Это свидетель, Рик, он нас сдаст, Рик\n'
				'—М-Морти... Хватит психовать, все будет нормаль... *отрыжка* нормально, Морти... Пошли домой.'
			)
			reply(locale_manager.get('rooms.default.usual.rick_and_morty.phrase_9'))
			reply(locale_manager.get('rooms.default.usual.rick_and_morty.phrase_10'))

			reply(locale_manager.get('rooms.default.usual.rick_and_morty.phrase_11'), photo='BQADAgADQwkAAmrZzgc2w-E75Bm4pwI')

			user.add_item('special', 'whisky')
			user.new_pet(reply, 'homeless')
		else:
			reply(locale_manager.get('rooms.default.usual.rick_and_morty.phrase_12'))
			reply(locale_manager.get('rooms.default.usual.rick_and_morty.phrase_13'), photo='BQADAgAD8AgAAmrZzgfsRAAB0r1hUeAC')

			user.reborn(reply, locale_manager.get('rooms.default.usual.rick_and_morty.phrase_14'), name=locale_manager.get('rooms.default.usual.rick_and_morty.phrase_15'))

def get_actions(user):
	question = user.get_room_temp('question', def_val='first')
	ans = [ ]

	if question == 'first':
		ans = [ READY, ESCAPE ]
	elif question == 'action':
		ans = [ HELLO, FIGHT ]

	random.shuffle(ans)

	return ans