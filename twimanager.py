import time
import random
import config
import tweepy
import constants
import usermanager
import databasemanager

auth = tweepy.OAuthHandler(config.CONSUMER_KEY, config.CONSUMER_SECRET)
auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

STATE = 'state'
ENTERED_UID = 'entered_name'
LAST_OPENED = 'last_opened'
TIME_TO_SLEEP = 30 * 60

def twi(text):
	try:
		api.update_status(text)
	except:
		pass

def get_phrase(ph_type, user):
	phrases = constant.twi_prhrases[ph_type]
	res = random.choice(phrases)
	return res.format(user.name)

def dead(user):
	twi(get_phrase('dead', user))
	databasemanager.set_variable(ENTERED_UID, 0)

def won(user):
	twi(get_phrase('won', user))
	databasemanager.set_variable(ENTERED_UID, 0)

def leave(user):
	if databasemanager.get_variable(ENTERED_UID, def_val=0) != 0:
		twi(get_phrase('leave', user))
		databasemanager.set_variable(ENTERED_UID, 0)

	databasemanager.set_variable(STATE, 'sleeps')

def enter(user):
	if not status()[0]:
		return False

	databasemanager.set_variable(STATE, 'busy')
	databasemanager.set_variable(LAST_OPENED, time.time())
	databasemanager.set_variable(ENTERED_UID, user.uid)

	twi(get_phrase('enter', user))

def last_opened():
	last_o = databasemanager.get_variable(LAST_OPENED, def_val=0)

	return time.time() - last_o

def status():
	return (False, 'sleeps')

"""
	state = databasemanager.get_variable(STATE, def_val='wait')
	
	if last_opened() > TIME_TO_SLEEP and state != 'wait':
		if state == 'busy':
			uid = databasemanager.get_variable(ENTERED_UID, def_val=0)
			if uid != 0:
				user = usermanager.get_user(uid)
				def foo(*a, **b):
					pass

				user.open_corridor(foor)
				usermanager.save_user(user)

		state = 'wait'
		databasemanager.get_variable(STATE, def_val='wait')

	return (state == 'wait', state)
"""
