from constants import *
import time
import databasemanager

name = 'Доктор кто'

hp = 25 * 1.01 ** (databasemanager.get_variable('doctor_num', 1) - 1)
damage_range =  ( 0, 50 )

coins = 0

loot = [ 'fez', 'laser_screwdriver' ]

def can_open(user, reply):
	return not user.has_tag(DEVIL)

def open_failure(user, reply):
	reply('Здесь не рады проклятым!')

def enter(user, reply):
	reply('Кто-кто?..')

	number = databasemanager.get_variable('doctor_num', 1)
	name = databasemanager.get_variable('doctor_killer')

	user.set_room_temp('hp_max', hp)

	reply('Я — _{0}_й Доктор!'.format(number), photo=DOCTOR_WHO_STICKER)

	if name is not None:
		t = time.time() - databasemanager.get_variable('doctor_kill_time', time.time()+1000)

		reply('Я реинкарнация после убийства доктора от руки игрока {0}'.format(name))

		if t > 0:
			reply('Моя новая реинкарнация длится уже {0:.2f} минут!'.format(t / 60))

def get_actions(user):
	return user.get_fight_actions() + [ 'Сдаться' ]

def make_damage(user, reply, dmg):
	hp = user.get_room_temp('hp', 0)
	hp -= max(1, dmg)

	if hp <= 0:
		number = databasemanager.get_variable('doctor_num', 1)
		databasemanager.set_variable('doctor_num', number + 1)
		databasemanager.set_variable('doctor_killer', user.name)
		databasemanager.set_variable('doctor_kill_time', time.time())

		databasemanager.add_to_leaderboard(user, user.get_room_temp('hp_max', 10 ** 5), databasemanager.DOCTOR_TABLE)
		user.won(reply)
	else:
		user.set_room_temp('hp', hp)

def action(user, reply, text):
	if text == 'Сдаться':
		reply('Доктор с ухмылкой сует Лазерную отвертку тебе в нос.')

		user.leave(reply)
	else:
		user.fight_action(reply, text)
