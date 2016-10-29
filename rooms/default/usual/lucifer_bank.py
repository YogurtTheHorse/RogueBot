import databasemanager

name = 'Банкиры Люцифера'

def get_actions(user):
	return [ 'Отдать', 'Придержать у себя' ]

def enter(user, reply):
	reply(
		'— Все мы знаем, что реинкарнация — не выдумка. Может быть, '
		'ты даже сам иногда чувствовал, что уже открывал эту дверь. '
		'Мы оказываем услугу трансинкарнационного перевода денег. С '
		'небольшой комиссией, конечно. Но вот какая штука. Чтобы душу '
		'действительно тряхнуло, ты должен расстаться сразу со всем золотом.',
		photo='BQADAgADSwkAAmrZzgc0tUQF067dNgI'
	)

def action(user, reply, text):
	if text == 'Отдать':
		if user.gold < 5000:
			reply('Маловато будет. Даже на комиссию не потянет.')
		else:
			user.gold = 0
			databasemanager.set_variable(str(user.uid) + '_gold', True)
			reply('С вами приятно иметь дело!')
	else:
		reply('Как знаешь.')

	user.leave(reply)
