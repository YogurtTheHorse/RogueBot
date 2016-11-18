name = 'Бомж'
description = ''
price = 0

def get_damage_bonus(user, reply):
	if user.has_item('whisky'):
		reply('Бомж атакует врага стыренными у парикмахера ножницами.')
		return 11
	else:
		reply('Нет виски — нет помощи.')
	return 0

def get_dice_bonus(user, reply):
	if user.has_item('whisky'):
		reply('Годы дворовой жизни научили Бомжа махинациям с игровыми костями.')
		return 7
	else:
		reply('Нет виски — нет помощи.')
		return 0

def on_room(user, reply, room):
	if room.room_type == 'monster' and room.hp > 120:
		reply('Ну нахрен, ты это вообще видел?! Я сваливаю. И виски заберу с собой!')
		user.remove_item('whisky')
		user.pet_gone()
	elif user.has_item('whisky'):
		reply('Допивать будете?')
