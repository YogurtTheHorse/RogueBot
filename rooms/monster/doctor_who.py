name = 'Доктор кто'

hp = 5000
damage_range =  ( 0, 50 )

coins = 0

loot = [ 'fez', 'laser_screwdriver' ]

def enter(user, reply):
	reply('Кто-кто?..')

def get_actions(user):
	return user.get_fight_actions() + [ 'Сдаться' ]

def action(user, reply, text):
	if text == 'Сдаться':
		reply('Доктор с ухмылкой сует Лазерную отвертку тебе в нос')

		user.leave(reply)
	else:
		user.fight_action(reply, text)