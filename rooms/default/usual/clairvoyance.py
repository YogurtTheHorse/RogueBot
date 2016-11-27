from localizations import locale_manager
import random
import usermanager
import rooms.roomloader as roomloader

name = locale_manager.get('rooms.default.usual.clairvoyance.phrase_4')

def enter(user, reply):
	reply(
		locale_manager.get('rooms.default.usual.clairvoyance.phrase_1'))

def get_actions(user):
	return [ locale_manager.get('rooms.default.usual.clairvoyance.phrase_5'), locale_manager.get('rooms.default.usual.clairvoyance.phrase_6') ]

def action(user, reply, text):
	if text == locale_manager.get('rooms.default.usual.clairvoyance.phrase_7'):
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
			reply(locale_manager.get('rooms.default.usual.clairvoyance.phrase_8'))
		else:
			name = found_user.name
			if found_user.pet:
				pet = found_user.get_pet()
				name += ' и {0} {1}'.format(pet.name, pet.real_name)

			res = locale_manager.get('rooms.default.usual.clairvoyance.phrase_9')

			if found_user.dead:
				res = locale_manager.get('rooms.default.usual.clairvoyance.phrase_10')
			elif found_user.state == 'corridor':
				res = locale_manager.get('rooms.default.usual.clairvoyance.phrase_11')
			elif found_user.state == 'pray':
				res = locale_manager.get('rooms.default.usual.clairvoyance.phrase_12')
			elif found_user.state == 'shop':
				res = locale_manager.get('rooms.default.usual.clairvoyance.phrase_13')
			elif found_user.state == 'inventory':
				res = locale_manager.get('rooms.default.usual.clairvoyance.phrase_14')
			elif found_user.state == 'room':
				res = (
					locale_manager.get('rooms.default.usual.clairvoyance.phrase_2'))

				room = roomloader.load_room(found_user.room[1], found_user.room[0], found_user)
				room_name = room.name

				res += room_name
			elif found_user.state == 'dice':
				res = (
					locale_manager.get('rooms.default.usual.clairvoyance.phrase_3'))

				room = roomloader.load_room(found_user.room[1], found_user.room[0], found_user)
				room_name = room.name

				res += room_name
			elif found_user.state == 'reborned':
				res = locale_manager.get('rooms.default.usual.clairvoyance.phrase_15') + str(found_user.reborn_answer) + '»'

			reply(res.format(name))
	else:
		user.leave(reply)
