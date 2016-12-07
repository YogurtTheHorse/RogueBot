from localizations import locale_manager
name = locale_manager.get('rooms.default.monster_medium.dipper.phrase_1')

hp = 60
damage_range = ( 3, 8 )

coins = 9

loot = [ ]


def make_damage(user, reply, dmg):
	hp = user.get_room_temp('hp', 0)
	hp -= dmg

	if hp <= 0:
		if not user.has_item('mystery_book_3'):
			reply(locale_manager.get('rooms.default.monster_medium.dipper.phrase_2'))
			user.add_item('special', 'mystery_book_3')
		user.won(reply)
	else:
		user.set_room_temp('hp', hp)

def enter(user, reply):
	reply(locale_manager.get('rooms.default.monster_medium.dipper.phrase_3'))

