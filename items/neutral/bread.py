from localizations import locale_manager
import random

name = locale_manager.get('items.neutral.bread.phrase_1')

price = 16

description = (
	locale_manager.get('items.neutral.bread.phrase_2')
)

fightable = True
disposable = True

def fight_use(user, reply, room):
	if room.code_name == 'duck':
		reply(locale_manager.get('items.neutral.bread.phrase_3'))
		user.new_pet(reply, 'duck')

		return 0
	else:
		reply(locale_manager.get('items.neutral.bread.phrase_4'))

		return 0