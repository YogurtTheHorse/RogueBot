import config
import collections
from tinydb import TinyDB, Query

VAR_TABLE = 'vars'
ROOMS_TABLE = 'rooms'
KILLS_TABLE = 'kills'
GNOME_TABLE = 'gnome'
RATE_TABLE = 'rate'

db = TinyDB(config.DATABASE_PATH)

def get_variable(name, def_val=None):
	global db
	Variable = Query()

	table = db.table(VAR_TABLE)
	ans = table.get(Variable.name == name)
	if ans:
		return ans['value']
	else:
		return def_val

def set_variable(name, value):
	global db
	Variable = Query()

	table = db.table(VAR_TABLE)
	if table.contains(Variable.name == name):
		table.update({'value':value}, Variable.name == name)
	else:
		table.insert({'name':name,'value':value})

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

	table.insert(doc)

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