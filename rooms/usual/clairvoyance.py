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
		usr = usermanager.random_user()
		res = 'Вижу.. Вижу.. {0}... Ничего не видно..'

		name = usr.name
		if usr.pet:
			pet = usr.get_pet()
			name += ' и {0} {1}'.format(pet.name, pet.real_name)

		if usr.dead:
			res = '{0} валяется мертвым на краю мира..'
		elif usr.state == 'corridor':
			res = '{0} пялится на коридор.'
		elif usr.state == 'pray':
			res = '{0} молится Богам.'
		elif usr.state == 'shop':
			res = '{0} затаривается вещичками.'
		elif usr.state == 'inventory':
			res = '{0} копается в инвентаре.'
		elif usr.state == 'room':
			res = (
				'{0} находится в комнате..\n\n'
				'И видит..\n'
			)

			room = roomloader.load_room(usr.room[1], usr.room[0])
			room_name = room.name

			res += room_name
		elif usr.state == 'dice':
			res = (
				'{0} находится в комнате..\n\n'
				'И бросает кости в..\n'
			)

			room = roomloader.load_room(usr.room[1], usr.room[0])
			room_name = room.name

			res += room_name
		elif usr.state == 'reborned':
			res = '{0} понимает, что «' + str(usr.reborn_answer) + '»'

		reply(res.format(name))
	else:
		user.leave(reply)
