import random
import usermanager
import items.itemloader as itemloader

from constants import *

name = 'Какой-то игрок'

actions = [ 'Ограбить', 'Уйти' ]

def get_actions(user):
	return actions

def enter(user, reply):
	users = list(usermanager.get_telegram_users())
	random.shuffle(users)

	user_id = None
	found_user = None

	for usr_id in users:
		usr = usermanager.get_user(usr_id)
		if not usr.dead and usr.get_time_from_last_message() < 5 * 60 and usr.uid != user.uid:
			user_id = usr_id
			found_user = usr
			break

	if found_user is not None:
		reply('Гоп стоп! Да это же {0}!'.format(found_user.name))
		user.set_room_temp('uid', found_user.uid)
		user.set_room_temp('steal_tries', 0)
	else:
		reply('Убежал куда-то..')
		user.leave(reply)

def steal(user, steal_user, is_last, reply):
	items = steal_user.get_items()

	if len(items) == 0:
		reply('Но в карманах было чуть меньше чем ничего. Вот неудача!')
		user.leave(reply)
		return

	item_to_steal = random.choice(items)

	reply('Ты стырил *{0}*!'.format(item_to_steal.name))

	user.add_item(item_to_steal.buff, item_to_steal.code_name)
	steal_user.remove_item(item_to_steal.code_name)
	steal_user.add_item('special', 'steal_note', {'stealer': user.name, 'item_name': item_to_steal.name})
	usermanager.save_user(steal_user)

	if is_last:
		user.leave(reply)


def dice(user, reply, result, subject=None):
	steal_tries = user.get_room_temp('steal_tries', 0)
	user.set_room_temp('steal_tries', steal_tries +1)

	p = 1 - 0.5 * (0.9 ** steal_tries)

	steal_user = usermanager.get_user(user.get_room_temp('uid'))
	if result >= DICE_MAX * p:
		reply('Ворюга ты конечно первоклассный.')
		steal(user, steal_user, result > DICE_MAX, reply)
	else:
		reply('Мда, вот тебя отмутохало-то.', photo='BQADAgAD1ggAAmrZzgenvIB-RsNAhwI')
		dmg = steal_user.get_damage()
		user.make_damage(1, dmg, reply, name='Воровство')


def action(user, reply, text):
	if text == actions[0]:
		user.throw_dice(reply)
	else:
		reply('Ты уходишь отсюда.')
		user.leave(reply)