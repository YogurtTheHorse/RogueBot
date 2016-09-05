import databasemanager
from rooms import roomloader
from datetime import datetime

SECONDS_WAIT = 60 * 60


def current():
  boss = databasemanager.get_variable('boss')

  if boss is None:
    return create()

  if __need_to_reborn(boss):
    return create(boss)

  return boss


def create(old_boss = None):
  boss_id = 1

  if old_boss is not None:
    boss_id = old_boss['id']

  room_type, room_name = roomloader.get_random_room('boss')
  room = roomloader.load_room(room_name, room_type)

  new_boss = {
    'id': boss_id + 1,
    'name': room_name,
    'alive': True,
    'hp': room.hp,
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


def __need_to_reborn(boss):
  if boss['die_seconds'] is None:
    return False

  seconds_passed = (datetime.now() - datetime(1970,1,1)).total_seconds() - boss['die_seconds']

  return boss['alive'] is False and seconds_passed > SECONDS_WAIT
