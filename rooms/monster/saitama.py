name = 'Сайтама'

hp = 300000
damage_range = (3000, 4000 )

coin = 0

loot = [ ]

def enter(user, reply):
	reply('Ты видишь лысого азиата в желтом костюме и красных перчатках.')

	if user.rooms_count < 50000:
		reply('Он быстро куда-то убежал, кажется он опаздывает на распродажу.')
		user.leave(reply)
	else:
		reply('Тебе не повезло, распродажи кончились.')
		
