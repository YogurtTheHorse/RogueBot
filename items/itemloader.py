import os
import imp
import random
import logging

logger = logging.getLogger('rg')

global user, context
user = None
context = { }

def get_user():
	global user
	return user

def get_context():
	global context
	return context

def load_item(name, buff, cntxt={}, usr=None):
	path = 'items/{0}/{1}.py'.format(buff, name)
	is_compiled = False

	if not os.path.exists(path):
		path += 'c'
		is_compiled = True
		if not os.path.exists(path):
			return None

	global user, context
	context = cntxt
	user = usr

	item = None
	if is_compiled:
		item = imp.load_compiled(name, path)
	else:
		item = imp.load_source(name, path)

	return check_item(item, name, buff) if item is not None else None

def check_item(item, name, buff):
	item.code_name = name
	item.buff = buff
	item.user = get_user()
	item.contex = get_context()

	required = [ 'name', 'description', 'price' ]

	for r in required:
		if not hasattr(item, r):
			logger.warn('Item "{0}" has no attribute {1}!'.format(name, r))
			return None

	defaults = [
		( lambda *args: None, [ 'on_room', 'on_enemy', 'on_escape', 'on_corridor', 'on_shop', 'on_pray', 'on_buy', 'on_dice', 'on_use', 'failure', 'success' ] ), # callbacks
		( lambda *args: 0, [ 'get_dice_bonus', 'get_damage_bonus', 'fight_use' ]),
		( lambda *args: True, [ 'can_use' ]),
		( 0, [ 'damage', 'mana_damage', 'charisma', 'defence' ] ), # buffs
		( '', [ 'aura', 'secret_desciption' ] ), # eeeh. meh
		( [ ], [ 'tags', 'loot' ] ), # some arrays?
		( False, [ 'usable', 'fightable', 'iscursed', 'disposable', 'strengthoff' ]),
		( 1, [ 'gold_bonus', 'shop_count' ] )
	]

	for def_val, names in defaults:
		for name in names:
			if not hasattr(item, name):
				setattr(item, name, def_val)

	return item

def get_all_items(buff):
	pth = 'items/' + buff + '/'
	items =  [ f[:-3] for f in os.listdir(pth) if f.endswith('.py') ]
	comp_items =  [ f[:-4] for f in os.listdir(pth) if f.endswith('.pyc') ]

	return items + comp_items

def load_random_item(buff):
	items = get_all_items(buff)

	return (buff, random.choice(items))

def load_shop_items():
	items = [
		load_random_item('bad'),
		load_random_item('good'),
		load_random_item('neutral')
	]

	it = load_random_item('good')
	while it in items:
		it = load_random_item('good')

	items.append(it)

	random.shuffle(items)

	return items

