import databasemanager

name = 'Гном в красной шапке'

def get_actions(user):
	actions = [ '10' ]
	g = 50
	while g < user.gold:
		actions.append(str(g))
		g += 50

	return actions[:min(10, len(actions))]


def enter(user, reply):
	reply('Выглядит порядочным и приятным молодым гномом.')

	reply('«Я могу обменять деньги на сильный и мощный артефакт. Чем больше ты отдашь, тем лучше будут его качества!»')

def action(user, reply, text):
	try:
		integer = int(text)

		if user.paid(integer) and integer > 0:
			reply('«Держи эту прекрасную ложку ручной работы!»')

			user.add_item('special', 'spoon')
			databasemanager.add_to_leaderboard(user, integer, databasemanager.GNOME_TABLE)
		else:
			reply('Вы ничего не поняли, но у вас исчезли деньги, а под глазом образовался синяк')
			user.gold = 0

		user.leave(reply)
	except:
		reply('Непонятное число у вас.')