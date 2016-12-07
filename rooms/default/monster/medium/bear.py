from localizations import locale_manager
name = locale_manager.get('rooms.default.monster_medium.bear.phrase_1')

hp = 70
damage_range =  ( 15, 30 )

coins = 50

loot = [ ]

def enter(user, reply):
	reply(locale_manager.get('rooms.default.monster_medium.bear.phrase_2'))

	if user.has_item('fish') or user.has_item('honey'):
		user.remove_item('fish')
		user.remove_item('honey')

		user.new_pet(reply, 'bear')
