from constants import *

name = 'Крыса'

hp = 20
element = NONE
damage_range =  ( 2, 4 )

def enter(user, reply):
	msg = (
		'ААААААААА! ТУТ КРЫСА. УБЕЙ ЕЕ.'
	)
	reply(msg)
