name = 'Драконий убийца'
description = (
	'Был вместо зуба у дракона, но теперь ты можешь использовать его по назначению.'
)

price = 1000

fightable = True

def fight_use(user, reply, room):
	if room.code_name == 'dragon' or room.code_name == 'quinquepede':
		reply('Это может показаться читерским, но ты выиграл этот поединок.')
		user.won(reply)

		return 0
	else:
		msg = (
			'Магическим и абстрактным образом этот меч отскочил от монстра и попал тебе в колено.\n'
			'Это же не дракон в конце концов.\n\n'
			'Зато теперь ты Дракон! Ну хотя бы твое колено..'
		)
		reply(msg)

		user.make_damage(20, 40, reply, name=name)

		return 0
