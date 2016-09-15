name = 'Дозоры'

actions_state_0		= [ 'Остановить бой', 'Уйти' ]  # Начало
actions_state_1		= [ 'Уйти' ] # Ушел
actions_state_2		= [ 'Уйти' ] # Остановил
# actions_state_3		= ['']
# actions_state_4		= ['']
# actions_state_5		= ['']
# actions_state_6		= ['']


def get_actions(user):
	if user.has_tag('watches_escape'):
		return actions_state_1
	elif user.has_tag('watches_stop'):
		return actions_state_2
	else:
		return actions_state_0


def enter(user, reply):

	if user.has_tag('watches_escape'):
		reply('Погибли все.')

	elif user.has_tag('watches_stop'):
		reply('Ты остановил бой. И заключили силы Света и силы Тьмы договор о перемирии.')

	else:
		reply(
			'C незапамятных времен рыцари, называющие себя воинами Света, '
			'ловят ведьм и колдунов, истязающих род человеческий. '
			'Но однажды на пути воинов Света встали воины Тьмы. '
			'И никто не хотел уступить. И начался бой кровавый и беспощадный. '
			'И когда битва дошла до Небес великий Гесер увидел что силы равны. '
			'И если не остановить бой — погибнут все... \n'
			)


def action(user, reply, text):

	if user.has_tag('watches_escape'):
		if text == actions_state_1[0]:
			reply('Тут больше нечего делать.')

	elif user.has_tag('watches_stop'):
		if text == actions_state_2[0]:
			reply('Возможно, скоро что-то случится, а пока пойдем дальше.')

	else:
		if text == actions_state_0[0]:
			reply(
				'И он остановил бой. И заключили силы Света и силы Тьмы договор о перемирии. '
				'И было сказано, что отныне ни добро ни зло нельзя творить без соглассия. '
				'И было сказано, что будет Дневной дозор, чтобы следить за силами Света. '
				'И было сказано, что будет Ночной дозор, чтобы следить за силами Тьмы.\n'
			)
			user.add_tag('watches_stop')

		else:
			reply('Правильно! Нечего вмешиватся в чужие разборки.')
			user.add_tag('watches_escape')

	user.leave(reply)

