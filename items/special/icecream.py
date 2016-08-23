import random 

name = "Мороженое"

description = (
	'Очень дорогое лакомство'
)

price = 30
tags = [ 'ice' ]

fightable = True

def fight_use(user, reply, room):
	reply('ЕЕЕЕЕ\nМороженное по лицу.\nИ режком по ребру_!_')
	
	return 15