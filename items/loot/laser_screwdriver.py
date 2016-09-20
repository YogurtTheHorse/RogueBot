import databasemanager

name = 'Лазерная отвертка'
description = '_Бжж-бжж_.'
price = 1000

defence = 100
damage = 100
mana_damage = 100

fightable = True

def on_room(user, reply, room):
	name = databasemanager.get_variable('doctor_killer')
	if user.name != name:
		reply('Кажется не ты настоящий Убийца Доктора.')
		user.remove_item('laser_screwdriver')

def fight_use(user, reply, room):
	reply('*Бжж-бжж*.')
	return 0