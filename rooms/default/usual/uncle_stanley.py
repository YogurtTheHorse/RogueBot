name = 'Дядя Стенли'

def get_actions(user):
	return ['Уйти']

def enter(user, reply):
	reply('Ты заходишь в комнату и видишь одноглазого старика с сундуком.\nОн вас заметил и обронив сундук, убежал.\nОткрыв сундук вы обнаруживаете там книгу с отпечатком шестипалой руки и цифрой 1')


def action(user, reply, text):
	if user.has_item('mystery_book_1'):
		reply('А. Такой у тебя уже есть.')
	else:
		user.add_item('special', 'mystery_book_1')

	user.leave(reply)
