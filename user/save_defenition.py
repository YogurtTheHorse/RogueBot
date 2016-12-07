import copy
import usermanager
from localizations import locale_manager

def save(self):
	self.set_variable('save', True)

def recover(self, reply):
	save = self.get_variable('save')

	if type(save) is dict or save is True:
		reply(locale_manager.get('messages.checkpoint', self.lang))

		self.set_variable('save', False)
		self.hp = self.max_hp // 2
		self.gold = self.gold // 2
		self.dead = False
		self.open_corridor(reply)