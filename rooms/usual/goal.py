from constants import DICE_MAX

name = 'Мишень'

actions = [ 'Попробовать попасть в нее', 'Уйти' ]

def get_actions(user):
	return actions

def dice(user, reply, result, subject=None):
	if result <= DICE_MAX:
		gold = 10 + result
		user.found(gold)
		reply('Держи золото: {0} монет'.format(gold))
	else:
		reply('Читатила! Стреляй в него!')
		user.make_damage(10, 30, reply, name='Кодекс чести лучников')
	user.leave(reply)

def action(user, reply, text):
	if text == actions[0]:
		user.throw_dice(reply)
	else:
		reply(
			'Ты повернулся спиной, а не спене у тебя оказалась _мишень_! Вот почему тебя хотят убить все! '
			'Ну а еще потому что это страшное подземлье — такие тут правила.\n'
			'В общем, в твою мишень прилетела стрела.'
		)
		user.make_damage(10, 30, reply, name='Какой-то лучник')
		user.leave(reply)