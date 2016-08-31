name = 'Единение'

price = 0
usable = True
# mana_damage = 0


def on_use(user, reply, shaman_level):
	# пока не придумал как реализовать едиение,
	# идея в том чтобы увеличивался mana_damage с каждым использованым духом.
	shaman_level += 1
	user.remove_item_by_name(name)

	if shaman_level >= 6:
		# mana_damage += 10
		print('Первая степень')

	elif 7 >= shaman_level >= 12:
		# mana_damage += 25
		print('Вторая степень')

	elif shaman_level >= 13:
		# mana_damage += 50
		print('Третья степень')
	else:
		print('Кажется ничего не изменилось')
