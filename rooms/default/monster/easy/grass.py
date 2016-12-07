from localizations import locale_manager
from constants import *

name = locale_manager.get('rooms.default.monster_easy.grass.phrase_1')

hp = 12
element = WATER
damage_range =  ( 0, 0 )

coins = 1

loot = [ ]

def enter(user, reply):
	msg = (
		locale_manager.get('rooms.default.monster_easy.grass.phrase_2')
	)
	reply(msg)

def get_actions(user):
	return user.get_fight_actions() + [ locale_manager.get('rooms.default.monster_easy.grass.phrase_3') ]

def action(user, reply, text):
	if text == locale_manager.get('rooms.default.monster_easy.grass.phrase_4'):
		reply(locale_manager.get('rooms.default.monster_easy.grass.phrase_5'))

		user.leave(reply)
	else:
		user.fight_action(reply, text)