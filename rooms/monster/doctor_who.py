import databasemanager

name = 'Доктор кто'

hp = 5000000
damage_range =  ( 0, 50 )

coins = 0

loot = [ 'fez', 'laser_screwdriver' ]

def enter(user, reply):
	reply('Кто-кто?..')

	number = databasemanager.get_variable('doctor_num', 11)

	reply('Я — _{0}_й Доктор!'.format(number))

def get_actions(user):
	return user.get_fight_actions() + [ 'Сдаться' ]

def make_damage(user, reply, dmg):
	hp = user.get_room_temp('hp', 0)
	hp -= max(1, dmg - user.rooms_count // 10)

	if hp <= 0:
		number = databasemanager.get_variable('doctor_num', 1)
		databasemanager.set_variable('doctor_num', number + 1)
		user.won(reply)
	else:
		user.set_room_temp('hp', hp)

def action(user, reply, text):
	if text == 'Сдаться':
		reply('Доктор с ухмылкой сует Лазерную отвертку тебе в нос.')

		user.leave(reply)
	else:
		user.fight_action(reply, text)
