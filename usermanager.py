import os
import glob
import pickle
import random
import config

from user import User
from localizations import locale_manager
		
def get_fname(uid):
	return config.USERS_PATH + '/{0}.usr'.format(uid)

def save_user(usr):
	if usr is None:
		return
		
	with open(get_fname(usr.uid), 'wb') as outfile:
		pickle.dump(usr, outfile)

def new_user(uid, nickname=None, reply=lambda *x, **y: None):
	usr = get_user(uid)

	if usr is None or usr.confirm_restart(reply):
		usr = User(uid)
		if nickname is not None:
			usr.nickname = nickname
		reply(locale_manager.get('main.whats_name', usr.lang))

	save_user(usr)

def random_user():
	return get_user(random.choice(list(get_telegram_users())))

def get_telegram_users():
	for f in glob.glob(config.USERS_PATH + '/*.usr'):
		uid = os.path.basename(f)[:-4]

		if not uid.startswith('vk'):
			yield uid

def delete(uid):
	if os.path.exists(get_fname(uid)):
		os.remove(get_fname(uid))

def get_user(uid):
	if os.path.exists(get_fname(uid)):
		usr = None

		with open(get_fname(uid), 'rb') as outfile:
			usr = pickle.load(outfile)

		return usr
	else:
		return None

def divine_intervention(uid, reply):
	usr = get_user(uid)
	usr.divine_intervention(reply)
	save_user(usr)

def message(uid, reply, text):
	usr = get_user(uid)

	if not usr:
		reply('Error. Try /start')
	elif usr.message(reply, text):
		usr = User(uid)

	save_user(usr)

def debug_info(uid):
	usr = get_user(uid)

	if not usr:
		return 'Error. Try /start'
	else:
		return usr.debug_info()

def setname(uid, name):
	usr = get_user(uid)
	usr.name = name
	save_user(usr)

def open_room(uid, reply, room_type, name):
	usr = get_user(uid)

	if not usr:
		reply('Error. Try /start')
	else:
		usr.open_room(reply, room_type, name)

	save_user(usr)

def give_item(uid, item_type, name):
	usr = get_user(uid)
	usr.add_item(item_type, name)
	save_user(usr)

def new_pet(uid, pet, name):
	usr = get_user(uid)
	usr.pet = (pet, name)
	save_user(usr)
