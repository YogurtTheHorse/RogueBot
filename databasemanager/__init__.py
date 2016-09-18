from pymongo import MongoClient
from databasemanager.leaderboard_model import get_model as get_leaderboard_model
from databasemanager.variable_model import get_model as get_variable_model
from databasemanager.lists_model import get_model as get_lists_model

client = MongoClient()
db = client['rogbot']

Leaderboards = get_leaderboard_model(db)
Variables = get_variable_model(db)
Lists = get_lists_model(db)

ROOMS_TABLE = 'rooms'
KILLS_TABLE = 'kills'
GNOME_TABLE = 'gnome'
ROULETTE_TABLE = 'roulette'
RATE_TABLE = 'rate'
DOCTOR_TABLE = 'doctor'

def get_variable(name, def_val=None):
	return Variables.get_value(name, def_val)

def set_variable(name, value):
	Variables.set_value(name, value)

def clear_list(name):
	Lists.clear_list(name)

def remove_from_list(name, val):
	Lists.remove_from_list(name, val)

def add_to_list(name, value, force=False):
	Lists.add_to_list(name, val, force)

def get_list(name):
	return Lists.get_list(name)

def add_to_leaderboard(user, score, leaderboard_name='rooms'):
	Leaderboards.add_to_leaderboard(user, score, leaderboard_name)

def get_leaderboard(leaderboard_name='rooms', count=10):
	return Leaderboards.get_leaderboard(leaderboard_name, count)
