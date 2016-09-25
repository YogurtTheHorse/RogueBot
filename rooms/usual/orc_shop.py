import usermanager

name = 'Торговец'

def enter(user, reply):
	usr = usermanager.random_user()
	msg = (
		'Перед тобой находится какая-то будка, неумело сколоченная из каких-то кривых досок. '
		'За широкой деревянной доской (прилавок) на воображаемой табуретке сидит зеленый бугай '
		'метра 2 ростом. Серьезно, он сидит в воздухе! Завидев тебя, он что-то нечленораздельно '
		'говорит, ты понимаешь лишь:\n'
		'«Привит, юдишка! Йа есть Боба! Босс сказал Бобе таргавать!! Боба типерь умеет в тарговлю!»\n\n'
		'Зуб (Цена 1 зуб)\n'
		'Тока што выбил с {0}, дажи кечтуп ищо капаит!\n\n'
		'Палка (Цена 5 зубов)\n'
		'Плахая палка, адной такой стукнул юдишку — а она сламалась\n\n'
		'Парашок (Цена 5 зубов)\n'
		'Вкусный парашок, клянусь Горком и Морком!'
	)
	reply(msg.format(usr.name))

def get_actions(user):
	return [ 'Зуб', 'Палка', 'Парашок', 'Уйти' ]

def action(user, reply, text):
	if text == 'Зуб':
		teeth_cnt = user.get_room_temp('teeth_cnt', def_val=0)


		if user.has_item('tooth'):
			if teeth_cnt > 2:
				reply('Ты давно понимаешь, что что-то идет не так, но орк выглядит вполне счастливым, и ты слышишь, как он бормочет что-то вроде: «какая харошая тарговля, босс будит даволен»')
			else:
				user.set_room_temp('teeth_cnt', teeth_cnt + 1)

			reply('Ты купил зуб! (И потратил на это зуб)')
		else:
			reply('«Нет зубов — нет товара» — хотел сказать орк, но просто ударил тебя по лицу.')
			user.make_damage(1, 10, reply, death=False)
	elif text == 'Палка':
		if user.items.count(('loot', 'tooth', {})) >= 5:
			reply('Забирай')
			user.add_item('good', 'mage_stick')

			for i in range(5):
				user.remove_item('tooth')
		else:
			reply('«Нет зубов — нет товара» — хотел сказать орк, но просто ударил тебя по лицу.')
			user.make_damage(1, 10, reply, death=False)
	elif text == 'Парашок':
		if user.items.count(('loot', 'tooth', {})) >= 5:
			reply('Забирай')
			user.add_item('neutral', 'protein')

			for i in range(5):
				user.remove_item('tooth')
		else:
			reply('«Нет зубов — нет товара» — хотел сказать орк, но просто ударил тебя по лицу.')
			user.make_damage(1, 10, reply, death=False)
	else:
		user.leave(reply)