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

	return migration(boss)


def migration(old_boss):
	if 'coins' not in old_boss:
		new_boss = {
			'id': old_boss.get('id', 1),
			'name': old_boss.get('name'),
			'alive': old_boss.get('alive'),
			'hp': old_boss.get('hp'),
			'max_hp': old_boss.get('hp'),
			'coins': 10000,
			'die_seconds': old_boss.get('die_seconds')
		}

		save(new_boss)

		return new_boss

	return old_boss


def create(old_boss=None):
	boss_id = 1

	if old_boss is not None:
		boss_id = old_boss['id']

	# Костыли, велосипеды
	# Тараканы, мотыльки
	room_name, hp, max_coins = random.choice([
		('black_knight', 129500, 51000 ),
		('hellkite_dragon', 175500, 71000),
		('moonlight_butterfly', 49500, 21000),
		('naping_dragon', 77500, 31000),
		('cthulhu', 575900, 251000),
		('lich_king', 325000, 141000)
	])
	new_boss = {
		'id': boss_id + 1,
		'name': room_name,
		'alive': True,
		'hp': hp,
		'max_hp': hp,
		'coins': random.randrange(1000, max_coins, 1),
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
		'max_hp': boss['max_hp'],
		'coins': boss['coins'],
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
