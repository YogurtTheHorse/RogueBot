from localizations import locale_manager
name = locale_manager.get('rooms.default.missions_caravan.army.phrase_1')

hp = 15000
damage_range =  ( 150, 200 )

coins = 7782

loot = [  ]
is_monster = True

def on_won(user, reply):
	reply(locale_manager.get('rooms.default.missions_caravan.army.phrase_2'))
	user.new_mission('caravan', 'caravan', path_len=75)
	user.set_room_temp('won', True)

def on_die(user, reply):
	user.new_mission('caravan', 'army', path_len=150)

def on_leave(user, reply):
	if not (user.get_room_temp('won') is True):
		reply(locale_manager.get('rooms.default.missions_caravan.army.phrase_3'))
		user.new_mission('caravan', 'army', path_len=150)

def enter(user, reply):
	msg = (
		locale_manager.get('rooms.default.missions_caravan.army.phrase_4'))
	reply(msg, photo='BQADAgAD5wgAAmrZzgcHFvPa24KvDwI')
