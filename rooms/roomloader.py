import os
import random
import logging
from importlib.machinery import SourceFileLoader
from importlib.machinery import SourcelessFileLoader

from constants import *

logger = logging.getLogger('rg')

def load_room(name, room_type='usual', user=None):
	path = 'rooms/{0}/{1}.py'.format(room_type, name)

	if not os.path.exists(path):
		path += 'c'
		if not os.path.exists(path):
			return None

	if path.endswith('c'):
		room_loader = SourcelessFileLoader(name, path)
	else:
		room_loader = SourceFileLoader(name, path)
	room = room_loader.load_module(name)

	return check_room(room, name, room_type)

def check_room(room, name, room_type):
	room.code_name = name
	room.room_type = room_type

	required = [ 'name', 'get_actions', 'action' ]

	if room_type == 'story':
		required.append('next_story_room_range')
		required.append('next_story_room')
	elif room_type == 'monster':
		required.append('damage_range')

		def get_actions(user):
			return user.get_fight_actions()

		def dice(user, reply, result, subject=None):
			return user.fight_dice(reply, result, subject)

		def action(user, reply, text):
			user.fight_action(reply, text)

		def make_damage(user, reply, dmg):
			hp = user.get_room_temp('hp', 0)
			hp -= dmg

			if hp <= 0:
				user.won(reply)
			else:
				user.set_room_temp('hp', hp)

		if not hasattr(room, 'get_actions'):
			setattr(room, 'get_actions', get_actions)

		if not hasattr(room, 'dice'):
			setattr(room, 'dice', dice)

		if not hasattr(room, 'action'):
			setattr(room, 'action', action)

		if not hasattr(room, 'make_damage'):
			setattr(room, 'make_damage', make_damage)

	for r in required:
		if not hasattr(room, r):
			logger.warn('Item "{0}" has no attribute {1}!'.format(name, r))
			return None

	defaults = [
		( lambda *args: None, [ 'enter', 'dice' ] ),
		( 0, [ 'coins' ] ),
		( 'none', [ ] ), 
		( NONE, [ 'element' ]),
		( [ ], [ 'loot' ] ),
		( False, [ ])
	]

	for def_val, names in defaults:
		for name in names:
			if not hasattr(room, name):
				setattr(room, name, def_val)

	return room

def get_next_room():
	p = random.random()

	if p < 1 / 100:
		return ('special', 'remains')
	elif p <= 0.5:
		return get_random_room('monster')
	else:
		return get_random_room('usual')

def get_random_room(room_type='usual'):
	pth = 'rooms/' + room_type + '/'
	rooms =  [ f[:-3] for f in os.listdir(pth) if f.endswith('.py') ]
	comp_rooms =  [ f[:-4] for f in os.listdir(pth) if f.endswith('.pyc') ]

	return (room_type, random.choice(rooms + comp_rooms))
