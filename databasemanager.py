import config
import collections

from tinydb import TinyDB, Query
from tinyrecord import transaction

ROOMS_TABLE = 'rooms'
KILLS_TABLE = 'kills'
GNOME_TABLE = 'gnome'
RATE_TABLE = 'rate'

VAR_TABLE = 'vars'
LIST_TABLE = '__list'
TORNAMENTS_TABLE = '__tor'

db = TinyDB(config.DATABASE_PATH)

def get_variable(name, def_val=None, table=VAR_TABLE):
	global db
	Variable = Query()

	table = db.table(VAR_TABLE)
	ans = table.get(Variable.name == name)
	if ans:
		return ans['value']
	else:
		return def_val

def set_variable(name, value, table=VAR_TABLE):
	global db
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

	table = db.table(LIST_TABLE)

	with transaction(table) as tr:
		tr.update({'value': [ ]}, ListQ.name == name)

	set_variable(name, [ ], table=LIST_TABLE)

def remove_from_list(name, val):
	lst = get_list(name)
	lst.remove(val)

	global db
	ListQ = Query()

	table = db.table(LIST_TABLE)
	with transaction(table) as tr:
		tr.update({'value': lst}, ListQ.name == name)

	set_variable(name, lst, table=LIST_TABLE)

def add_to_list(name, value, force=False):
	global db
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
	ListQ = Query()

	table = db.table(LIST_TABLE)
	ans = table.get(ListQ.name == name)
	if ans:
		return ans['value']
	else:
		return [ ]


def add_to_leaderboard(user, score, leaderboard_name='rate'):
	global db

	table = db.table(leaderboard_name)
	doc = {
		'uid': user.uid,
		'name': user.name,
		'score': score
	}
	if hasattr(user, 'death_reason'):
		doc['death_reason'] = user.death_reason


	with transaction(table) as tr:
		tr.insert(doc)

def get_leaderboard(leaderboard_name='rate', count=10):
	global db

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