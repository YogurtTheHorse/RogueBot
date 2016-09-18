import databasemanager
import usermanager
import logging
import random
import time

logger = logging.getLogger('rg')

def add_to_list(tornament_name, uid):
	num = databasemanager.add_to_list(tornament_name, uid)
	databasemanager.add_to_list('tor_names', tornament_name)

	if num < -1:
		return False

	return True

def get_tornament(tid):
	def_val = get_tornament_dict(tid, [ ])
	return databasemanager.get_variable(tid, def_val=def_val)

def get_tornament_dict(tid, uids):
	names = [ ]
	for uid in uids:
		usr = usermanager.get_user(uid)
		if usr:
			names.append(usr.name)

	return {
		'id': tid,
		'users': uids,
		'names': names
	}

def save_tornament(tid, uids):
	val = get_tornament_dict(tid, uids)
	databasemanager.set_variable(tid, val)

def start_tornament(tornament_name, reply):
	uids = databasemanager.get_list(tornament_name)
	databasemanager.clear_list(tornament_name)

	tornament_id = str(round(time.time() * 1000))
	tornament_dict = get_tornament_dict(tornament_id, uids)

	save_tornament(tornament_id, uids)
	databasemanager.add_to_list('tors', tornament_id)

	for uid in uids:
		def rep(txt, btns=None, photo=None):
			reply(uid, txt, btns, photo)
		usr = usermanager.get_user(uid)
		if usr:
			usr.start_tornament(tornament_id, rep)
			usermanager.save_user(usr)


def update(reply):
	tors = databasemanager.get_list('tors')
	names = databasemanager.get_list('tor_names')

	for name in names:
		lst = databasemanager.get_list(name)
		if len(lst) > 9:
			start_tornament(name, reply)

	for tornament_id in tors:
		update_tornament(reply, tornament_id)

def update_tornament(reply, tid):
	tornament = get_tornament(tid)
	uids = tornament['users']

	users = [ usermanager.get_user(uid) for uid in uids ]

	def get_next_user(i):
		next_i = (i + 1) %  len(users)
		while users[next_i].dead:
			next_i = (i + 1) %  len(users)

		return next_i

	if len(users) == 1:
		user = users[0]

		def rep(txt, btns=None, photo=None):
			reply(user.uid, txt, btns, photo)

		databasemanager.remove_from_list('tors', tornament['id'])

		gold = random.randint(10000, 20000)

		rep('Это победа! Цезарь дарует тебе *{0}* злт.'.format(gold))
		user.give_gold(gold)
		user.open_corridor(rep)

		usermanager.save_user(user)
	else:
		msg = ''

		for i, user in enumerate(users):
			dmg = user.get_room_temp('damage', def_val=0)
			user.set_room_temp('damage', 0)
			user.set_room_temp('attacked', False)
			next_i = get_next_user(i)

			if next_i != i:
				def rep(txt, btns=None, photo=None):
					reply(users[next_i].uid, txt, btns, photo)
				users[next_i].make_damage(dmg, dmg, rep)
				usermanager.save_user(users[next_i])
				msg += '{0} нанес {1} ед. урона игроку {2}\n'.format(user.name, dmg, users[next_i].name)

			usermanager.save_user(user)

		msg += '\nПродолжаем резню!'

		for user in users:
			if not user.dead:
				reply(user.uid, msg)
			else:
				uids.remove(user.uid)
				reply(user.uid, 'Тебя постигло поражение. Так держать!', ['/start'])

		save_tornament(tid, uids)


		

def make_damage(user, reply, dmg):
	if user.get_room_temp('attacked', def_val=False):
		reply('Ты уже атаковал. Подожди какое-то время.')
	else:
		user.set_room_temp('attacked', True)
		user.set_room_temp('damage', dmg)

		reply('А теперь жди.')