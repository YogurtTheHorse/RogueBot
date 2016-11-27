from localizations import locale_manager
import random
from items import itemloader
from utils import costumes

name = locale_manager.get('rooms.default.special.helloween_shop.phrase_1')

ACTIONS = [ locale_manager.get('rooms.default.special.helloween_shop.phrase_2'), locale_manager.get('rooms.default.special.helloween_shop.phrase_3'), locale_manager.get('rooms.default.special.helloween_shop.phrase_4')]

def enter(user, reply):
	reply(
		locale_manager.get('rooms.default.special.helloween_shop.phrase_5'))

	user.set_room_temp('costume', costumes.rand_costume_key())

def get_actions(user):
	return ACTIONS

def action(user, reply, text):
	if text == ACTIONS[0]:
		reply(locale_manager.get('rooms.default.special.helloween_shop.phrase_6'), photo='BQADAgAD7QgAAmrZzgfDVlphbK6MlgI')
		user.add_item('special', 'pumpkin')
		user.leave(reply)
	elif text == locale_manager.get('rooms.default.special.helloween_shop.phrase_7'):
		reply(locale_manager.get('rooms.default.special.helloween_shop.phrase_8'))
		user.add_item('special', 'candle')
		user.leave(reply)
	elif text == ACTIONS[1]:
		key = user.get_room_temp('costume', 'none')
		costume = costumes.get_costume(key)

		user.costume = key

		reply(locale_manager.get('rooms.default.special.helloween_shop.phrase_9'))
		reply('_Вы надеваете костюм {0}_'.format(costume['who']))
		reply(costume['description'])
	elif text == ACTIONS[2]:
		reply(locale_manager.get('rooms.default.special.helloween_shop.phrase_10'))

		user.add_item('special', 'candy')
	else:
		reply(locale_manager.get('rooms.default.special.helloween_shop.phrase_11'))
		return

	user.leave(reply)
