name = 'Река'


def get_actions(user):
	return [ 'Грести', 'Вернуться в джунгли' ]


def enter(user, reply):
	reply(
		'Ты решаете осмотреться и замечаещь лодку, стоящую неподалёку.\n'
		'Тебе ничего не остается, кроме как прыгнуть в речку и плыть. Да, всё именно так.\n'
		'Хотя можно просто вернуться обратно в Джунгли..'
	)
	user.set_room_temp('rvr', 0)

def action(user, reply, text):
	if text == 'Вернуться в джунгли':
		user.leave(reply)
		return

	rvr = user.get_room_temp('rvr', 0)

	if user.has_item('m79') :
		rvr += 4
		reply('Ты вспоминаешь, что у тебя есть М79, берешь его в руки и гребешь.')
	else:
		rvr += 1
		reply('Ты гребешь руками. Кажется, что скоро конец')
	
	user.set_room_temp('rvr', rvr)

	if rvr > 8:
		msg = ''
		if user.has_item('m-16'):
			user.remove_item('m-16')
			reply('Твой М-16 теперь не стреляет.. Пишлость выкинуть.')


		reply(
			'Вы пристаете к другому концу берега, вылезаете из лодки.\n'
			'Единственное место, куда вы можете пойти здесь - едва приоткрытая дверь.\n'
			'Вы открываете дверь... И выходите в Коридор!\n\n'
		)

		user.rooms_pack = 'default'
		user.leave(reply)
