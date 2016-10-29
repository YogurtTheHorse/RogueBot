name = 'ОБЪЕДИНЕННАЯ АРМИЯ ПОДЗЕМЕЛЬЯ'

hp = 15000
damage_range =  ( 150, 200 )

coins = 7782

loot = [  ]
is_monster = True

def on_won(user, reply):
	reply('Вы составили мирный договор. Ждите поставок с севера!')
	user.new_mission('caravan', 'caravan', path_len=75)
	user.set_room_temp('won', True)

def on_die(user, reply):
	user.new_mission('caravan', 'army', path_len=150)

def on_leave(user, reply):
	if not (user.get_room_temp('won') is True):
		reply('Мы еще догоним тебя.. Потом.')
		user.new_mission('caravan', 'army', path_len=150)

def enter(user, reply):
	msg = (
		'Перед тобой 1337 война. Мне кажется у кого-то большие проблемы.'
	)
	reply(msg, photo='BQADAgAD5wgAAmrZzgcHFvPa24KvDwI')
