from constants import *

FIGHT = 'За Шир!!!'
ESCAPE = 'Попытаться убежать'

name = 'Темный лорд'
hp = 1000  # Темный Лорд должен быть лютым парнем! А то что-то они там все перекаченные какие-то.
damage_range = ( 20, 25 )

coins = 0  # Темному Лорду не нужны деньги! Он берет все что захочет!

loot = [ 'ring' ]


def enter(user, reply):
	reply(
		'Кажется мы оказались не в том месте в не то время.\n'
		'Очень надеюсь что {} не обратит на нас внимание.'.format(name),
		photo='BQADAgAD_ggAAmrZzgfWmyCl_kraUgI'
	)

	if user.rooms_count < 500000:
		reply(
			'Кажется он вас не заметил.\n'
			'Вот и славненько, пойдем отсюда скорее, не будем мешать.'
		)

		user.leave(reply)

	else:

		if not user.has_item('ring'):
			reply(
				'Апчих!\n'
				'Как тут пыльно!\n'
				'ОЙ! По Моему нас заметили!'
			)

		else:
			user.remove_item('ring')  # У игрока должно быть только одно кольцо!
			reply(
				'«_Я чувстую его! Оно мое!_»\n'
				'Мамочки! Мне страшно!\n'
				'Верни ему то что он просит! НЕМЕДЛЕННО!'
			)
		user.leave(reply)


def dice(user, reply, result, subject=None):

	if subject == ESCAPE:

		if result > DICE_MIDDLE:
			reply('Тебе удалось! Надеюсь мы больше не встретим этого мерзкого типа!')
			user.leave(reply)

		else:
			reply('Не вышло!\nНу ни чего я буду за тебя болеть!')
			# тут нужно запустить обычый бой


def action(user, reply, text):
	question = user.get_room_temp('question')

	if text == FIGHT:
		reply(
			'Пойду ка я спрячусь вон за ту колонну! '
			'А вы тут пока общайтесь!'
		)
		# тут нужно запустить обычый бой


	elif text == ESCAPE:
		reply(
			'«_Апчих! Пора тут прибарться_»\n'
			'Кидай кубики, это наш шанс!!!'
		)
		user.throw_dice(reply, ESCAPE)


def get_actions(user):
	return [FIGHT, ESCAPE]
