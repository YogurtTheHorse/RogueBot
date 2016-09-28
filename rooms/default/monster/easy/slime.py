from constants import *

name = 'Слизень'

hp = 30
element = WATER
damage_range =  ( 0, 3 )

coins = 3

loot = [ 'slime' ]

def enter(user, reply):
	msg = (
		'Это слизень. Самый обычный слизень.'
	)
	reply(msg, photo=SLIME_STICKER)

def get_actions(user):
	return [ 'Раздавить' ] + user.get_fight_actions()

def action(user, reply, text):
	if text == 'Раздавить':
		reply('Ты раздавил его, но запачкал обувь.')

		if user.has_item('intoxicated_shoes'):
			user.add_tag('dirt')

			if user.tags.count('dirt') > 10:
				user.remove_item('intoxicated_shoes')
				user.tags = list(filter(('dirt').__ne__, user.tags))

		user.won(reply)
	else:
		user.fight_action(reply, text)