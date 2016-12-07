from localizations import locale_manager
name = locale_manager.get('rooms.default.monster_medium.promote.phrase_1')

hp = 100
damage_range =  ( 15, 17 )

coins = 17

loot = [ ]

def enter(user, reply):
	reply(locale_manager.get('rooms.default.monster_medium.promote.phrase_2'))
	reply(locale_manager.get('rooms.default.monster_medium.promote.phrase_3'), photo='BQADAgADCgkAAmrZzgetbDY3dR3FjQI')

def get_actions(user):
	return user.get_fight_actions() + [ locale_manager.get('rooms.default.monster_medium.promote.phrase_4') ]

def action(user, reply, text):
	if text == locale_manager.get('rooms.default.monster_medium.promote.phrase_5'):
		reply(locale_manager.get('rooms.default.monster_medium.promote.phrase_6'))

		user.steal(150)
		user.leave(reply)
	else:
		user.fight_action(reply, text)