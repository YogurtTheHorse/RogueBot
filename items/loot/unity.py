name = 'Единение'

price = 0
usable = True


def on_use(user, reply, shaman_level):
	shaman_level += 1
	user.remove_item_by_name(name)

	if shaman_level >= 6:
		print('Первая степень')

	elif 7 >= shaman_level >= 12:
		print('Вторая степень')

	elif shaman_level >= 13:
		print('Третья степень')

	else:
		print('Кажется ничего не изменилось')
