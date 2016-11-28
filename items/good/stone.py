from localizations import locale_manager
import items.itemloader as itemloader

name = locale_manager.get('items.good.stone.phrase_1')
context = itemloader.get_context()

price = 50
usable = not ('message' in context)

if 'message' in context:
	description = locale_manager.get('items.good.stone.phrase_2') + str(context['message'])
else:
	description = locale_manager.get('items.good.stone.phrase_3')

	usable = True
	disposable = True

	def on_use(user, reply):
		reply(locale_manager.get('items.good.stone.phrase_4'))
		user.open_room(reply, 'special', 'stone_room')