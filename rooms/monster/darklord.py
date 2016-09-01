from random import randrange

name = 'Темный лорд'
hp = 500
damage_range = ( 20, 25 )

coins = randrange(200, 400, 10)

loot = [ 'ring' ]


def enter(user, reply):
	reply(
		'Кажется мы оказались не в том месте в не то время.\n'
		'Очень надеюсь что {} не обратит на нас внимание.'.format(name)
	)

	if user.story_level < 10:
		reply(
			'Кажется, он вас не заметил.\n'
			'Вот и славненько, пойдем отсюда скорее, не будем мешать'
		)
		user.leave(reply)

	else:
		reply(
			'Апчих!\n'
			'Как тут пыльно!\n'
			'ОЙ! По Моему нас заметили!'
		)