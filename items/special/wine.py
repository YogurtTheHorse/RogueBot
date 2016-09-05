import random

name = 'Винцо'

description = (
	'Бутылка отличного вина. Немного испачкана в иле. '
	'Божественный вкус.'
)

price = 300
fightable = True
disposable = True

def fight_use(user, reply, room):
	reply('ЗА ВДВ!')

	if random.random() < 0.3 or room.code_name == 'doctor_who':
		reply('Это было больно.')
		user.death(reply, reason=name)

		return 0
	else:
		reply('Противник попятился назад. Это победа!')
		user.won(reply)

		return 0
