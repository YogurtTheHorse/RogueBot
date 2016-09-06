import databasemanager
import random
from datetime import datetime

SECONDS_WAIT = 60 * 60


def current():
	boss = databasemanager.get_variable('boss')

	if boss is None:
		return create()

	if need_to_reborn(boss):
		return create(boss)

	return boss


def create(old_boss = None):
	boss_id = 1

	if old_boss is not None:
		boss_id = old_boss['id']

	# Костыли, велосипеды
	room_name, hp = random.choice([('black_knight', 129500), ('hellkite_dragon', 175500), ('moonlight_butterfly', 49500), ('naping_dragon', 77500)])
	new_boss = {
		'id': boss_id + 1,
		'name': room_name,
		'alive': True,
		'hp': hp,
		'die_seconds': None
	}

	save(new_boss)

	return new_boss


def die(boss):
	new_boss = {
		'id': boss['id'],
		'name': boss['name'],
		'alive': False,
		'hp': 0,
		'die_seconds': (datetime.now() - datetime(1970,1,1)).total_seconds()
	}

	save(new_boss)


def save(boss):
	databasemanager.set_variable('boss', boss)

def need_to_reborn(boss):
	if boss['die_seconds'] is None:
		return False

	seconds_passed = (datetime.now() - datetime(1970,1,1)).total_seconds() - boss['die_seconds']

	return boss['alive'] is False and seconds_passed > SECONDS_WAIT
