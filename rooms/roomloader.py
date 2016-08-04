import os
import random
import logging
from importlib.machinery import SourceFileLoader

logger = logging.getLogger('rg')

def load_room(name, room_type='usual', user=None):
	path = 'rooms/{0}/{1}.py'.format(room_type, name)

	if not os.path.exists(path):
		return None

	room_loader = SourceFileLoader(name, path)
	room = room_loader.load_module(name)

	return check_room(room, name, room_type)

def check_room(room, name, room_type):
	room.code_name = name
	room.room_type = room_type

	required = [ 'name', 'get_actions', 'room_type', 'action' ]

	for r in required:
		if not hasattr(room, r):
			logger.warn('Item "{0}" has no attribute {1}!'.format(name, r))
			return None

	def foo(*arg):
		pass

	defaults = [
		( foo, [ 'enter', 'dice' ] ),
		( 0, [ ] ),
		( 'none', [ ] ), 
		( [ ], [ ] ),
		( False, [ ])
	]

	for def_val, names in defaults:
		for name in names:
			if not hasattr(room, name):
				setattr(room, name, def_val)

	return room

def get_random_room(room_type='usual'):
	pth = 'rooms/' + room_type + '/'
	rooms =  [ f[:-3] for f in os.listdir(pth) if f.endswith('.py') ]

	return (room_type, random.choice(rooms))
