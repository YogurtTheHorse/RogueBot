from constants import *

name = 'Трава'

hp = 12
element = WATER
damage_range =  ( 0, 0 )

coins = 1

loot = [ ]

def enter(user, reply):
	msg = (
		'Это трава в горшке.'
	)
	reply(msg)

def get_actions(user):
	return user.get_fight_actions() + [ 'Уйти' ]

def action(user, reply, text):
	if text == 'Уйти':
		reply('Ты просто ушел от травы.')

		user.leave(reply)
	else:
		user.fight_action(reply, text)