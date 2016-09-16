from constants import *

name = 'Печать Чистоты'

description = ('Печать в виде черепа, к ней прикреплены 2 длинных листочка с Литаниями Богу-Императору Всего Человечества.\nКак сказал алхимик ее нужно крепить прямо на себя.')

price = 50

defence = 1

def on_pray(user, reply, god):
	if god == EMPEROR_NUM:
		user.gods_level[EMPEROR_NUM] += 1