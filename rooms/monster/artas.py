name = 'Король Лич'
hp = 300
damage_range = ( 100, 120 )
loot = [ 'frostmourne' ]

def enter(user, reply):
	if user.rooms_count < 500:
		reply('Жалкая курица, пшел вон!')
		user.leave(reply)
	else:
		reply('«Неужели прибыли, наконец, хваленные силы света? Мне бросить ледяную скорбь и сдаться на твою милость, герой?»')
