from localizations import locale_manager
from constants import *

name = locale_manager.get('rooms.default.monster_easy.slime.phrase_1')

hp = 30
element = WATER
damage_range =  ( 0, 3 )

coins = 3

loot = [ 'slime' ]

def enter(user, reply):
	msg = (
		locale_manager.get('rooms.default.monster_easy.slime.phrase_2')
	)
	reply(msg, photo=SLIME_STICKER)

def get_actions(user):
	return [ locale_manager.get('rooms.default.monster_easy.slime.phrase_3') ] + user.get_fight_actions()

def action(user, reply, text):
	if text == locale_manager.get('rooms.default.monster_easy.slime.phrase_4'):
		reply(locale_manager.get('rooms.default.monster_easy.slime.phrase_5'))

		if user.has_item('intoxicated_shoes'):
			user.add_tag('dirt')

			if user.tags.count('dirt') > 10:
				user.remove_item('intoxicated_shoes')
				user.tags = list(filter(('dirt').__ne__, user.tags))

		user.won(reply)
	else:
		user.fight_action(reply, text)