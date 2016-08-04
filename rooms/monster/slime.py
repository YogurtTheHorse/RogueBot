from constants import *

name = 'Слизень'

hp = 30
element = WATER
damage_range =  ( 0, 3 )

def enter(user, reply):
	msg = (
		'Это слизень. Самый обычный слизень.'
	)
	reply(msg)
