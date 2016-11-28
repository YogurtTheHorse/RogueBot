from localizations import locale_manager
import random

from utils.buffs import DiabetBuff

name = locale_manager.get('items.special.candy.phrase_1')
description = (
	locale_manager.get('items.special.candy.phrase_2')
)

price = 1

usable = True
disposable = True

def on_use(user, reply):
	cnt = user.get_variable('candies_eat', 0)

	if cnt == 10:
		reply(locale_manager.get('items.special.candy.phrase_3'))
		reply(locale_manager.get('items.special.candy.phrase_4'))

		user.new_buff(DiabetBuff())
		user.add_item('special', 'candy')
	elif cnt == 11:
		reply(locale_manager.get('items.special.candy.phrase_5'))
		user.add_item('special', 'candy')
		user.make_damage(3, 7, reply, name=locale_manager.get('items.special.candy.phrase_6'))
	elif cnt > 11:
		reply(locale_manager.get('items.special.candy.phrase_7'))
		user.make_damage(cnt - 5, cnt + 3, reply, name=locale_manager.get('items.special.candy.phrase_8'))
	else:
		reply(locale_manager.get('items.special.candy.phrase_9'))
		user.heal(15)

	user.get_variable('candies_eat', cnt + 1)