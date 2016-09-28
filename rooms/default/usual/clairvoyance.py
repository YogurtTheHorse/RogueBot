import random
import usermanager
import rooms.roomloader as roomloader

name = 'Шар'

def enter(user, reply):
	reply(
		'Дверь за вами исчезла, повеяло холодом. Вы оказались в '
		'огромном зале, с тусклым светом исходящим издали. Сотни '
		'шаров, расставленных на постаментах по всему '
		'безграничному залу, отбрасывают мрачные тени.'
	)

def get_actions(user):
	return [ 'Посмотреть в шар', 'Идти на свет' ]

def action(user, reply, text):
	if text == 'Посмотреть в шар':
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

		if found_user is None:
			reply('Ничего не видно..')
		else:
			name = found_user.name
			if found_user.pet:
				pet = found_user.get_pet()
				name += ' и {0} {1}'.format(pet.name, pet.real_name)

			res = 'Вижу.. Вижу.. {0}... Ничего не видно..'

			if found_user.dead:
				res = '{0} валяется мертвым на краю мира..'
			elif found_user.state == 'corridor':
				res = '{0} пялится на коридор.'
			elif found_user.state == 'pray':
				res = '{0} молится Богам.'
			elif found_user.state == 'shop':
				res = '{0} затаривается вещичками.'
			elif found_user.state == 'inventory':
				res = '{0} копается в инвентаре.'
			elif found_user.state == 'room':
				res = (
					'{0} находится в комнате..\n\n'
					'И видит..\n'
				)

				room = roomloader.load_room(found_user.room[1], found_user.room[0], found_user)
				room_name = room.name

				res += room_name
			elif found_user.state == 'dice':
				res = (
					'{0} находится в комнате..\n\n'
					'И бросает кости в..\n'
				)

				room = roomloader.load_room(found_user.room[1], found_user.room[0], found_user)
				room_name = room.name

				res += room_name
			elif found_user.state == 'reborned':
				res = '{0} понимает, что «' + str(found_user.reborn_answer) + '»'

			reply(res.format(name))
	else:
		user.leave(reply)
