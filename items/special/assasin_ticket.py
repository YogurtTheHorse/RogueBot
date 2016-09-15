name = 'Талончик на убийство'
description = 'Одноразовая штука. Осторожнее с ним.'
price = 0

disposable = True
fightable = True

def fight_use(user, reply, room):
	reply('Ты моргнул, а противн получил *9000* урона.')

	return 9000