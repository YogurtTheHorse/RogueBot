import random

name = 'Рыцарь'

hp = 170
damage_range =  ( 30, 40 )

coins = 170

loot = [ random.choice(['shield', 'knight_helmet', 'knight_sword', 'knight_knee']) ]

def enter(user, reply):
	reply('Весь в доспехах')

	if user.story_level < 3:
		reply('Я не бью маленьких деочек типа тебя')
		user.leave(reply)
