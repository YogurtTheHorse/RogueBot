import copy
import usermanager

def save(self):
	self.set_variable('save', True)

def recover(self, reply):
	save = self.get_variable('save')

	if type(save) is dict or save is True:
		reply('О, чекпоинт! В этот раз никто не умер, но впредь будьте осторожнее')

		self.set_variable('save', False)
		self.hp = self.max_hp // 2
		self.gold = self.gold // 2
		self.dead = False
		self.open_corridor(reply)