import items.itemloader as itemloader

name = 'Булыжник'
context = itemloader.get_context()

price = 50
usable = not ('message' in context)

if 'message' in context:
	description = 'На нем написано:\n' + str(context['message'])
else:
	description = 'Можно кидать в других игроков!'

	usable = True
	disposable = True

	def on_use(user, reply):
		reply('Взяв булыжник ты отправляешься в какую-то комнату..')
		user.open_room(reply, 'special', 'stone_room')