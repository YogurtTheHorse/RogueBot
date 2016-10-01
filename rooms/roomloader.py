import os
import random
import logging
import bossmanager
from importlib.machinery import SourceFileLoader
from importlib.machinery import SourcelessFileLoader

from constants import *

logger = logging.getLogger('rg')

def load_room(name, room_type='usual', user=None):
	path = 'rooms/{0}/{1}/{2}.py'.format(user.rooms_pack if user is not None else 'default', room_type, name)

	if not os.path.exists(path):
		path += 'c'
		if not os.path.exists(path):
			return None

	import_name = (room_type + '.' + name).replace('/', '.');

	if path.endswith('c'):
		room_loader = SourcelessFileLoader(import_name, path)
	else:
		room_loader = SourceFileLoader(import_name, path)

	room = room_loader.load_module(import_name)

	return check_room(room, name, room_type)

def check_room(room, name, room_type):
	room.code_name = name
	room.room_type = room_type

	required = [ 'name', 'get_actions', 'action' ]

	if room_type.startswith('monster') or (hasattr(room, 'is_monster') and room.is_monster):
		room.room_type = 'monster'
		required.append('damage_range')

		def get_actions(user):
			return user.get_fight_actions()

		def dice(user, reply, result, subject=None):
			return user.fight_dice(reply, result, subject)

		def action(user, reply, text):
			user.fight_action(reply, text)

		def make_damage(user, reply, dmg):
			hp = user.get_room_temp('hp', 0)
			hp -= max(1, dmg)

			if hp <= 0:
				user.won(reply)
			else:
				user.set_room_temp('hp', hp)

		if not hasattr(room, 'get_actions'):
			setattr(room, 'get_actions', get_actions)

		if not hasattr(room, 'dice'):
			setattr(room, 'dice', dice)

		if not hasattr(room, 'action'):
			setattr(room, 'action', action)

		if not hasattr(room, 'make_damage'):
			setattr(room, 'make_damage', make_damage)

	elif room_type == 'boss':
		required.append('damage_range')

		def enter(user, reply):
			msg = (
				'*Ахххр-гр!*\n'
			)

			reply(msg)

			boss = bossmanager.current()

			user.set_room_temp('boss_id', boss['id'])

		def get_actions(user):
			return user.get_fight_actions() + [ 'Уйти' ]

		def dice(user, reply, result, subject=None):
			return user.fight_dice(reply, result, subject)

		def action(user, reply, text):
			boss = bossmanager.current()
			user_boss_id = user.get_room_temp('boss_id')

			if text == 'Уйти':
				if boss.get('id') is not user_boss_id:
					user.leave(reply)

				else:
					if boss.get('alive'):
						msg = (
							'Густой туман не дает тебе выйти.\n'
							'У босса осталось {} HP.'.format(boss['hp'])
						)

						reply(msg)

					else:
						if user.get_room_temp('was_received_reward', def_val=False) is False:
							msg = (
								'Ты ушел, но на мгновение тебе показалось, что ты не забрал свой трофей.\n'
								' — Да не, бред какой-то, — и ты продолжил свой путь к коридору.'
							)

							reply(msg)

						user.leave(reply)

			else:
				user_damage = user.get_room_temp('user_damage', def_val=0)

				user.fight_action(reply, text)

				if user.state == 'room':

					if user_damage > 0 and boss.get('alive') and boss.get('id') is user_boss_id and boss.get('max_hp') // user_damage < 10:
						skill_damage = room.skill(user, reply, boss)

						if skill_damage > 0:
							user.make_damage(skill_damage, skill_damage, reply, defence=False, name=room.name)

		def give_reward(user, reply, boss):
			if user.get_room_temp('was_received_reward', def_val=False) is False:
				user.set_room_temp('was_received_reward', True)

				user.won(reply, boss=boss)
				room.on_die(user, reply)

			else:
				msg = (
					'Ты можешь и дальше продолжать избивать мертвую тушу, но зачем?'
				)

				reply(msg)
				user.leave(reply)


		def skill(user, reply, boss):
			if random.random() < 0.55:
				msg = (
					'Ты пытаешься увернуться и ...'
				)

				room.skill_preparing(user, reply, boss)

				reply(msg)

				if random.random() < 0.75:
					msg = (
						'У тебя не получилось.\n'
						'Босс попадает в тебя и наносит *{}* урона'
					)

					room.skill_success(user, reply, boss)

					min_dmg, max_dmg = room.damage_range
					damage = random.randrange(min_dmg, max_dmg, 1)

					reply(msg.format(damage))

					return damage

				else:
					msg = (
						'Тебе это удалось!'
					)

					room.skill_failure(user, reply, boss)

					reply(msg)

			return 0


		def make_damage(user, reply, dmg):
			boss = bossmanager.current()
			user_boss_id = user.get_room_temp('boss_id')
			user_damage = user.get_room_temp('user_damage', def_val=0)

			if boss['id'] == user_boss_id:
				if boss['hp'] > 0:
					boss['hp'] -= dmg

					user.set_room_temp('user_damage', user_damage + dmg)

					if boss['hp'] <= 0:
						bossmanager.die(boss)
						give_reward(user, reply, boss)
					else:
						msg = (
							'У босса осталось {} HP.'.format(boss['hp'])
						)

						reply(msg)

						bossmanager.save(boss)

				else:
					msg = (
						'Ты ударил мертвую тушу и ничего не произошло.\n'
						'Так же ты заметил, что туман позади тебя исчез.\n'
					)

					reply(msg)
					give_reward(user, reply, boss)

			else:
				msg = (
					'Ты ударил в пустоту, но зачем?'
				)

				reply(msg)

		if not hasattr(room, 'enter'):
			setattr(room, 'enter', enter)

		if not hasattr(room, 'get_actions'):
			setattr(room, 'get_actions', get_actions)

		if not hasattr(room, 'dice'):
			setattr(room, 'dice', dice)

		if not hasattr(room, 'action'):
			setattr(room, 'action', action)

		if not hasattr(room, 'give_reward'):
			setattr(room, 'give_reward', give_reward)

		if not hasattr(room, 'skill'):
			setattr(room, 'skill', skill)

		if not hasattr(room, 'make_damage'):
			setattr(room, 'make_damage', make_damage)

	for r in required:
		if not hasattr(room, r):
			logger.warn('Item "{0}" has no attribute {1}!'.format(name, r))
			return None

	defaults = [
		( lambda *args: None, [ 'enter', 'dice',  'on_death', 'on_leave', 'on_won', 'on_die', 'skill_preparing', 'skill_success', 'skill_failure', 'open_failure' ] ),
		( 0, [ 'coins' ] ),
		( 'none', [ ] ), 
		( NONE, [ 'element' ] ),
		( [ ], [ 'loot' ] ),
		( lambda *args: True, [ 'can_open' ] ),
		( False, [ 'not_for_sign' ] )
	]

	for def_val, names in defaults:
		for name in names:
			if not hasattr(room, name):
				setattr(room, name, def_val)

	return room

def get_next_room(user):
	if user is not None:
		if user.get_last_mission().is_ready():
			mission = user.get_last_mission()
			return (mission.get_room_type(), mission.get_room_name())

	p = random.random()

	if p < 1 / 100:
		return ('special', 'remains')
	elif p <= 0.7:
		return get_random_room('monster/' + user.level, user, 'monster')
	else:
		return get_random_room('usual', user)

def get_all_rooms(rooms_pack, room_type):
	pth = 'rooms/' + rooms_pack + '/' + room_type + '/'

	rooms =  [ f[:-3] for f in os.listdir(pth) if f.endswith('.py') ]
	comp_rooms =  [ f[:-4] for f in os.listdir(pth) if f.endswith('.pyc') ]

	return rooms + comp_rooms

def get_level_rooms(user, level):
	all_visited_rooms = user.get_perma_variable('visited_rooms', [ ])
	names = [ ]
	rm_type = 'monster/' + str(level)

	for rm in get_all_rooms(user.rooms_pack, rm_type):
		if rm in all_visited_rooms:
			room = load_room(rm, rm_type, user)
			names.append(room.name)
		else:
			names.append('?' * 5)

	return names

def get_random_room(room_type, user, second_type=None):
	rooms = [ (room_type, rm) for rm in get_all_rooms(user.rooms_pack, room_type) ]

	if second_type is not None:
		rooms.extend([ (second_type, rm) for rm in get_all_rooms(user.rooms_pack, second_type) ])

	all_visited_rooms = user.get_perma_variable('visited_rooms', [ ])

	not_visited_rooms = [ ]
	visited_rooms = [ ]

	for tp, rm in rooms:
		if rm in all_visited_rooms:
			visited_rooms.append((tp, rm))
		else:
			not_visited_rooms.append((tp, rm))
	
	visited_rooms_proc = len(visited_rooms) / len(rooms)

	if len(not_visited_rooms) > 0:
		new_room = random.choice(not_visited_rooms)
	else:
		user.prepare_boss()
		new_room = random.choice(rooms)

	return new_room
