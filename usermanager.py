import os
import glob
import pickle
import random
from user import User
		
def get_fname(uid):
	return 'users/{0}.usr'.format(uid)

def save_user(usr):
	with open(get_fname(usr.uid), 'wb') as outfile:
		pickle.dump(usr, outfile)

def new_user(uid):
	usr = User(uid)

	save_user(usr)

def random_user():
	return get_user(random.choice(list(get_telegram_users())))

def get_telegram_users():
	for f in glob.glob('users/*.usr'):
		uid = ''
		try:
			uid = f.split('/')[1][:-4]
		except:
			uid = f.split('\\')[1][:-4]

		if not uid.startswith('vk'):
			yield uid

def get_user(uid):
	if os.path.exists(get_fname(uid)):
		usr = None

		with open(get_fname(uid), 'rb') as outfile:
			usr = pickle.load(outfile)

		return usr
	else:
		return None

def message(uid, reply, text):
	usr = get_user(uid)

	if not usr:
		reply('Что-то пошло не так. Попробуй /start')
	else:
		usr.message(reply, text)

	save_user(usr)

def debug_info(uid):
	usr = get_user(uid)

	if not usr:
		return 'Что-то пошло не так. Попробуй /start'
	else:
		return usr.debug_info()

def setname(uid, name):
	usr = get_user(uid)
	usr.name = name
	save_user(uid)


def open_room(uid, reply, room_type, name):
	usr = get_user(uid)

	if not usr:
		reply('Что-то пошло не так. Попробуй /start')
	else:
		usr.open_room(reply, room_type, name)

	save_user(usr)

def give_item(uid, item_type, name):
	usr = get_user(uid)
	usr.add_item(item_type, name)
	save_user(usr)
