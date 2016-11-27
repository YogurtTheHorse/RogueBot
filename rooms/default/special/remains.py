from localizations import locale_manager
import random
import usermanager
import items.itemloader as itemloader

from collections import Counter

from constants import REMAINS_STICKER

name = locale_manager.get('rooms.default.special.remains.phrase_1')

actions = [ locale_manager.get('rooms.default.special.remains.phrase_2'), locale_manager.get('rooms.default.special.remains.phrase_3')]

def get_actions(user):
	return actions

def enter(user, reply):
	users = list(usermanager.get_telegram_users())
	random.shuffle(users)

	user_id = None
	found_user = None

	for usr_id in users:
		usr = usermanager.get_user(usr_id)
		if usr.dead:
			user_id = usr_id
			found_user = usr
			break

	if found_user is not None:
		reply('Здесь лежат останки игрока {0}'.format(found_user.name), photo='BQADAgADFwkAAmrZzgf5q0m1CmsDggI')
		user.set_room_temp('items', found_user.items)
	else:
		reply(locale_manager.get('rooms.default.special.remains.phrase_4'), photo='BQADAgADFwkAAmrZzgf5q0m1CmsDggI')
		user.leave(reply)


def action(user, reply, text):
	if text == actions[0]:
		items = [ (it[0], it[1]) for it in user.get_room_temp('items', def_val=[]) if len(it) < 3 or len(it[2]) == 0 ]

		if len(items) == 0:
			reply(locale_manager.get('rooms.default.special.remains.phrase_5'))
		else:
			reply(locale_manager.get('rooms.default.special.remains.phrase_6'))

			user.give_gold(random.randrange(12, 72))

			items.append(('loot', 'tooth'))
			items.append(('loot', 'tooth'))

			for it in items:
				user.add_item(it[0], it[1])

			counter_items = Counter(items)
			items_str = [ ]
			for it, cnt in counter_items.most_common():
				loaded_item = itemloader.load_item(it[1], it[0], usr=user)
				if loaded_item is not None:
					items_str.append('*{0}* ({1} шт.)'.format(loaded_item.name, cnt))

			reply('Его рюкзак вмещал в себя следующие вещи: {0}'.format(', '.join(items_str)))

	else:
		reply(locale_manager.get('rooms.default.special.remains.phrase_7'))
		
	user.leave(reply)
