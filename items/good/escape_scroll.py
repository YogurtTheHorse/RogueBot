from localizations import locale_manager
import random

name = locale_manager.get('items.good.escape_scroll.phrase_4')

description = (
	locale_manager.get('items.good.escape_scroll.phrase_1'))

price = 9990
fightable = True
disposable = True


def success(user, reply, room):
	msg = (
		locale_manager.get('items.good.escape_scroll.phrase_2'))

	reply(msg)


	if user.gold > 0:
		msg = (
			locale_manager.get('items.good.escape_scroll.phrase_3'))

		coins = user.gold // 2

		user.steal(coins)

		reply(msg.format(coins))

	user_items = user.get_items()

	item = random.choice(user_items)

	if user_items and item.name is not name:
		msg = (
			locale_manager.get('items.good.escape_scroll.phrase_5')
		)

		user.remove_item_by_name(item.name)

		reply(msg.format(item.name))

	user.leave(reply)