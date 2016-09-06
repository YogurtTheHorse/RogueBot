import random

import logging
from constants import *

from localizations import locale_manager
import usermanager

def name_confirm(self, reply, text):
	if len(text) == 7:
		txt = locale_manager.get('NAME_CONFIRMED').format(self.name)
		self.state = 'first_msg'

		logger.info('New user with id {0}'.format(self.uid))

		reply(txt, [ locale_manager.get('WHATS_NEXT') ])
	else:
		self.state = 'name'
		reply(locale_manager.get('ASK_NAME_AGAIN'))

def name_given(self, reply, name):
	if '_' in name:
		reply(locale_manager.get('NAME_ERROR'))
	else:
		n = name
		while n == name:
			usr = usermanager.random_user()
			n = usr.name

		msg = locale_manager.get('NAME_CONFIRM').format(n, name)

		buttons = [ locale_manager.get('NAME_AGREE'), locale_manager.get('NAME_DISMISS') ]
			
		self.state = 'name_confirm'
		self.name = name

		reply(msg, buttons)

def first(self, reply, text):
	reply(locale_manager.get('HELLO_MESSAGE'))

	self.open_corridor(reply)