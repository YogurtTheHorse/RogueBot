name = 'Гном в красной шапке'

def get_actions(user):
	actions = [ '10' ]
	g = 50
	while g < user.gold:
		actions.append(str(g))
		g += 50

	return actions


def enter(user, reply):
	reply('Выглядит порядочным и приятным молодым гномом.')

	reply('«Я могу обменять деньги на сильный и мощный артефакт. Чем больше ты отдашь, тем лучше будут его качества!»')

def action(user, reply, text):
	try:
		integer = int(text)

		if user.paid(integer):
			reply('«Держи эту прекрасную ложку ручной работы!»')

			user.add_item('special', 'spoon')
		else:
			reply('Вы ничего не поняли, но у вас исчезли деньги, а под глазом образовался синяк')
			user.gold = 0

		user.leave(reply)
	except:
		reply('Непонятное число у вас.')