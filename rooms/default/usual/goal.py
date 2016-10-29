from constants import DICE_MAX

name = 'Мишень'

actions = [ 'Попробовать попасть в нее', 'Уйти' ]


def get_actions(user):
	return actions


def dice(user, reply, result, subject=None):
	if result <= DICE_MAX:
		msg = (
			'Держи золото: {0} монет.'
		)

		gold = 10 + result

		reply(msg.format(gold))
		user.give_gold(gold)

	else:
		msg = (
			'Читатила! Стреляй в него!'
		)

		reply(msg, photo='BQADAgAD3wgAAmrZzgdOxgndC2991gI')
		user.make_damage(10, 30, reply, name='Кодекс чести лучников')

	user.leave(reply)


def action(user, reply, text):
	if text == actions[0]:
		user.throw_dice(reply)

	else:
		msg = (
			'Ты повернулся спиной, а не спине у тебя оказалась _мишень_! Вот почему тебя хотят убить все!\n'
			'Ну, а еще потому, что это страшное подземелье — такие тут правила.\n'
			'В общем, в твою _мишень_ прилетела стрела.'
		)

		reply(msg, photo='BQADAgAD3wgAAmrZzgdOxgndC2991gI')
		user.make_damage(10, 30, reply, name='Какой-то лучник')
		user.leave(reply)
