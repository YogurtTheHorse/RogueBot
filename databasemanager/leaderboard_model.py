import pymongo

from bson.code import Code

from collections import Counter

from mongothon import Schema
from mongothon import create_model
from mongothon.validators import one_of

from utils import costumes

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
		if leaderboard == 'death':
			res = list(cls.find({"leaderboard": 'rooms'}))

			keyf = Code("function(doc) {return{\"death_reason\": doc.death_reason}}")
			reducer = Code("function(curr, result) { result.count++; }")
			
			res = list(cls.get_collection().group( 
				key = keyf, 
				condition = {
					"death_reason": { "$exists": True },
					"leaderboard": "rate"
				}, 
				reduce = reducer, 
				initial = { "count": 0}
			))

			def sort_death(doc):
				return -doc['count']

			res.sort(key=sort_death)

			return res[:count]
		else:
			def sort_by_score(doc):
				return doc['score']

			cursor = cls.find({"leaderboard": leaderboard})
			sorted = cursor.sort('score', pymongo.DESCENDING)
			res = list(sorted.limit(count))

			return res[:count]
		return list(cls.find({"leaderboard": leaderboard}))[:count]

	@Scores.class_method
	def add_to_leaderboard(cls, user, score, leaderboard_name='rooms'):
		name = user.name

		costume = costumes.get_costume(user.costume)
		name += ' в костюме _{0}_'.format(costume['who'])

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
