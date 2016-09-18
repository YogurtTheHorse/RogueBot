from mongothon import Schema
from mongothon import create_model
from mongothon.validators import one_of

ROOMS_TABLE = 'rooms'
KILLS_TABLE = 'kills'
GNOME_TABLE = 'gnome'
ROULETTE_TABLE = 'roulette'
RATE_TABLE = 'rate'
DOCTOR_TABLE = 'doctor'

TABLES = [ ROOMS_TABLE, KILLS_TABLE, GNOME_TABLE, ROULETTE_TABLE, RATE_TABLE, DOCTOR_TABLE ]

score_schema = Schema({
		'uid': {'type': str, 'required': True},
		'name': {'type': str, 'required': True},
		'score': {'type': int, 'required': True},
		'leaderboard': {'type': str, 'validates': one_of(*TABLES)},
		'death_reason': {'type': str }
	})

def get_model(db):
	Scores = create_model(score_schema, db['scores'])

	@Scores.class_method
	def get_leaderboard(cls, leaderboard, count=10):
		return list(cls.find({"leaderboard": leaderboard}))[:count]

	@Scores.class_method
	def add_to_leaderboard(cls, user, score, leaderboard_name='rooms'):
		name = user.name
		if user.pet:
			pet = user.get_pet()
			name += ' и {0} {1}'.format(pet.name, pet.real_name)

		doc = {
			'uid': user.uid,
			'name': name,
			'score': score,
			'leaderboard': leaderboard_name
		}
		if hasattr(user, 'death_reason'):
			doc['death_reason'] = user.death_reason

		cls.insert(doc)

	return Scores