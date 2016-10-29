name = 'Дракон'

hp = 140
damage_range =  ( 15, 30 )

coins = 300

loot = [ 'dragon_sword' ]

def enter(user, reply):
	reply('Большой и красный, как в сказке.', photo='BQADAgADywgAAmrZzgeQZg8qNy8d0AI')

	if user.rooms_count < 50:
		reply('Он не заметил тебя и прошел мимо. Мелкий еще.')
		user.leave(reply)
