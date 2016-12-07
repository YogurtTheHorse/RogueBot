from localizations import locale_manager
name = locale_manager.get('rooms.default.monster_medium.nazgul.phrase_2')

hp = 100
damage_range = ( 10, 15 )

coins = 130

loot = [ ]


def enter(user, reply):
	reply(locale_manager.get('rooms.default.monster_medium.nazgul.phrase_3'))

	if user.rooms_count < 75:
		reply(locale_manager.get('rooms.default.monster_medium.nazgul.phrase_4').format(name))
		user.leave(reply)

	else:
		reply(
			locale_manager.get('rooms.default.monster_medium.nazgul.phrase_1'))
