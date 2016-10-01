from constants import *

name = 'Крыса-летяга'

hp = 15
element = NONE
damage_range =  ( 5, 7 )

coins = 12

loot = [ 'bat_wing' ]

def enter(user, reply):
	msg = (
		'Тут у нас _мышь!_.\n'
		'*Летучая*.\n\n'
		'Слабая, но бьет больно.'
	)
	reply(msg, photo=BAT_STICKER)
