import re
import random

from utils.names import antimat

import logging
from constants import *

import databasemanager

from localizations import locale_manager
import usermanager

logger = logging.getLogger('rg')

def name_confirm(self, reply, text):
	if len(text) == 7:
		txt = locale_manager.get('NAME_CONFIRMED').format(self.name)
		self.state = 'first_msg'

		logger.info('New user with id {0}'.format(self.uid))

		self.set_perma_variable('name', text)

		reply(txt, [ locale_manager.get('WHATS_NEXT') ])
	else:
		self.state = 'name'
		reply(locale_manager.get('ASK_NAME_AGAIN'))

def name_given(self, reply, name):
	if not only_letters(name) or len(name) <= 0:
		reply(locale_manager.get('NAME_ERROR'))
	else:
		n = name
		while n == name:
			usr = usermanager.random_user()
			n = usr.name

		msg = locale_manager.get('NAME_CONFIRM').format(n, name)

		buttons = [ locale_manager.get('NAME_AGREE'), locale_manager.get('NAME_DISMISS') ]
			
		self.state = 'name_confirm'
		self.name = antimat(name)

		reply(msg, buttons)

def first(self, reply, text):
	reply(locale_manager.get('HELLO_MESSAGE'))

	mn = databasemanager.get_variable(str(self.uid) + '_gold')

	if mn is not None and mn:
		databasemanager.set_variable(str(self.uid) + '_gold', False)
		reply('Вы не помните даже кем вы были в той жизни, а вот мы замечательно помним, что получили от вас ровно тысячу. Да. Точно-точно. Нет, не развод.')
		self.give_gold(1000)

	self.open_corridor(reply)

def only_letters(tested_string):
    match = re.match(u"^[A-Za-z0-9\u0400-\u0500 ]*$", tested_string)
    return match is not None
