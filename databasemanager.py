import config
from tinydb import TinyDB, Query

VAR_TABLE = 'vars'
ROOMS_TABLE = 'rooms'
KILLS_TABLE = 'kills'

db = TinyDB(config.DATABASE_PATH)

def get_variabe(name, def_val=None):
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
	
	table = db.table(VAR_TABLE)
	return table.insert({'name':name,'value':value})

def add_to_lederboard(user, score, lederboard_name='rooms'):
	global db
	
	table = db.table(lederboard_name)
	doc = {
		'uid': user.uid,
		'name': user.name,
		'score': score
	}
	table.insert(doc)

def get_lederboard(lederboard_name='rooms', count=10):
	global db
	
	def sort_by_score(doc):
		return doc['score']

	table = db.table(lederboard_name)

	res = table.all()
	res.sort(key=sort_by_score)

	return res[:count]