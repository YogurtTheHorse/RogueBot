import random

name = 'Ледяная скорбь'
description = 'Тот кто держит этот клинок, должен обладать бесконечной силой. Подобно тому, как он разрывает плоть, он разрывает души.'
price = 500

fightable = True

def fight_use(user, reply, room):
	if random.random() < 0.3:
		reply('Ледяная скорбь поглотила вашу душу.')
		user.death(reply, reason=name)

		return 0

	return 150