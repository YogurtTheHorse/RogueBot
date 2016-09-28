import random

name = 'Король лич'

hp = 325000
damage_range = ( 80, 160 )

coins = random.randrange( 1000, 141000, 1)


def skill_preparing(user, reply, boss):
	reply('Склонись перед своим господином и повелителем!')
	