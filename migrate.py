import config
import asyncio
import collections
import threading

from tinydb import TinyDB, Query
from tinyrecord import transaction

ROOMS_TABLE = 'rooms'
KILLS_TABLE = 'kills'
GNOME_TABLE = 'gnome'
ROULETTE_TABLE = 'roulette'
RATE_TABLE = 'rate'
DOCTOR_TABLE = 'doctor'

VAR_TABLE = 'vars'
LIST_TABLE = '__list'
TORNAMENTS_TABLE = '__tor'

global db, db_lock
try:
	db is None
	db_lock is None
except:
	db = TinyDB(config.DATABASE_PATH)
	db_lock = threading.RLock()


def get_variable(name, def_val=None, table=VAR_TABLE):
	global db

	with db_lock:
		Variable = Query()

		table = db.table(VAR_TABLE)
		ans = table.get(Variable.name == name)
		if ans:
			return ans['value']
		else:
			return def_val

def set_variable(name, value, table=VAR_TABLE):
	global db

	with db_lock:
		Variable = Query()

		table = db.table(VAR_TABLE)
		with transaction(table) as tr:
			if table.contains(Variable.name == name):
				tr.update({'value':value}, Variable.name == name)
			else:
				tr.insert({'name':name,'value':value})

def clear_list(name):
	global db
	ListQ = Query()

	with db_lock:
		table = db.table(LIST_TABLE)

		with transaction(table) as tr:
			tr.update({'value': [ ]}, ListQ.name == name)

		set_variable(name, [ ], table=LIST_TABLE)

def remove_from_list(name, val):
	lst = get_list(name)
	lst.remove(val)

	global db
	with db_lock:
		ListQ = Query()

		table = db.table(LIST_TABLE)
		with transaction(table) as tr:
			tr.update({'value': lst}, ListQ.name == name)

	set_variable(name, lst, table=LIST_TABLE)

def add_to_list(name, value, force=False):
	global db
	with db_lock:
		ListQ = Query()

		lst = [ ]

		table = db.table(LIST_TABLE)
		ans = table.get(ListQ.name == name)
		if ans:
			lst = ans['value']

		res = len(lst)

		if value not in lst or force:
			lst.append(value)
		else:
			res = -1

		with transaction(table) as tr:
			if ans:
				tr.update({'value':lst}, ListQ.name == name)
			else:
				tr.insert({'name':name,'value':lst})

	return res

def get_list(name):
	global db
	with db_lock:
		ListQ = Query()

		table = db.table(LIST_TABLE)
		ans = table.get(ListQ.name == name)
		if ans:
			return ans['value']
		else:
			return [ ]


def add_to_leaderboard(user, score, leaderboard_name='rooms'):
	global db

	name = user.name
	if user.pet:
		pet = user.get_pet()
		name += ' и {0} {1}'.format(pet.name, pet.real_name)

	with db_lock:
		table = db.table(leaderboard_name)
		doc = {
			'uid': user.uid,
			'name': name,
			'score': score
		}
		if hasattr(user, 'death_reason'):
			doc['death_reason'] = user.death_reason


		with transaction(table) as tr:
			tr.insert(doc)

def get_leaderboard(leaderboard_name='rooms', count=10):
	global db

	with db_lock:
		if leaderboard_name == 'death':
			counter = collections.Counter()
			table = db.table(RATE_TABLE)
			res = table.all()

			for r in res:
				if 'death_reason' in r and str(r['death_reason']) != 'None':
					counter.update([r['death_reason']])

			return counter.most_common(count)
		else:
			if leaderboard_name not in db.tables():
				return [ ]

			def sort_by_score(doc):
				return doc['score']

			table = db.table(leaderboard_name)

			res = table.all()
			res.sort(key=sort_by_score, reverse=True)

			return res[:count]

import databasemanager
#from pymongo import Connection
#c = Connection()
#c.drop_database('rogbot')

print('Moving variables..')
for variable in db.table(VAR_TABLE).all():
	databasemanager.set_variable(variable['name'], variable['value'])
	print('\tMoved "{0}" = {1}.'.format(variable['name'], variable['value']))
	
print('We don\'t migrate lists..')

new_leaderboards = databasemanager.Leaderboards

for leaderboard_name in [ ROOMS_TABLE, KILLS_TABLE, GNOME_TABLE, ROULETTE_TABLE, RATE_TABLE, DOCTOR_TABLE ]:
	print('\tMigrating "{0}" leaderboard...'.format(leaderboard_name))
	lst = db.table(leaderboard_name).all()
	len_lst = len(lst)
	for ind, res in enumerate(lst):
		print('\t\t{0}%'.format(100 * ind / len_lst))
		res['leaderboard'] = leaderboard_name
		new_leaderboards.insert(res)
	print('\tDone!')
