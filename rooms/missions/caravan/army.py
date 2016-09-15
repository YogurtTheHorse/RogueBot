name = 'ОБЪЕДИНЕННАЯ АРМИЯ ПОДЗЕМЕЛЬЯ'

hp = 15000
damage_range =  ( 150, 200 )

coins = 13782

loot = [  ]
is_monster = True

def enter(user, reply):
	msg = (
		'Перед тобой 1337 война. Мне кажется у кого-то большие проблемы.'
	)
	reply(msg)

def make_damage(user, reply, dmg):
	hp = user.get_room_temp('hp', 0)
	hp -= max(1, dmg - user.rooms_count // 10)

	if hp <= 0:
		reply('Ты победил, но мы еще вернемся.')
		user.new_mission('caravan', 'army', path_len=75)
		user.won(reply)
	else:
		user.set_room_temp('hp', hp)
