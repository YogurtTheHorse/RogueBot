from constants import *

name = 'Крыса'

hp = 15
element = NONE
damage_range =  ( 5, 7 )

def enter(user, reply):
	msg = (
		'Тут у нас _мышь!_\n'
		'*Летучая*.\n\n'
		'Слабая, но бьет больно'
	)
	reply(msg)
