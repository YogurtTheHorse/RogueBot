name = 'Механочерепаха'
hp = 200
damage_range = (10, 12)

loot = [ 'mechanic_shell' ]

def enter(user, reply):
	reply('Пшш...скрскр....псцшшшщ...', photo='BQADAgADCwkAAmrZzgca3p47J9mzpAI')

	if user.rooms_count < 35:
		reply('Она шипя ушла в другую комнату.')
		user.leave(reply)