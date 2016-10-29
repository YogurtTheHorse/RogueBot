name = 'Промоутер'

hp = 100
damage_range =  ( 15, 17 )

coins = 17

loot = [ ]

def enter(user, reply):
	reply('Он в костюме пачки сигарет «Мальберт». Он выглядит весьма упоротым и почему-то кружится на месте.')
	reply('Сегодня его выкуривали несколько раз. Он будет мстить.', photo='BQADAgADCgkAAmrZzgetbDY3dR3FjQI')

def get_actions(user):
	return user.get_fight_actions() + [ 'Начать кружится с ним' ]

def action(user, reply, text):
	if text == 'Начать кружится с ним':
		reply('Ты укружился обратно в коридор. А в карманах стало меньше денег.')

		user.steal(150)
		user.leave(reply)
	else:
		user.fight_action(reply, text)