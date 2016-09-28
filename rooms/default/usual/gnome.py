from constants import *
import databasemanager

name = 'Гном в красной шапке'

def get_actions(user):
	actions = [ '10' ] + [ str((g + 1) * 50) for g in range(min(user.gold // 50, 9)) ]

	return actions

def can_open(user, reply):
	return not user.has_tag(DEVIL)

def open_failure(user, reply):
	reply('Здесь не рады проклятым!')

def enter(user, reply):
	reply('Выглядит порядочным и приятным молодым гномом.\n-Я могу обменять деньги на сильный и мощный артефакт. Чем больше ты отдашь, тем лучше будут его качества!')

def action(user, reply, text):
	try:
		integer = int(text)

		if user.paid(integer) and integer > 0:
			reply('«Держи эту прекрасную ложку ручной работы!»')

			user.add_item('special', 'spoon')
			databasemanager.add_to_leaderboard(user, integer, databasemanager.GNOME_TABLE)
		else:
			reply('Вы ничего не поняли, но у вас исчезли деньги, а под глазом образовался синяк.')
			user.gold = 0

		user.leave(reply)
	except:
		reply('Непонятное число у вас.')
