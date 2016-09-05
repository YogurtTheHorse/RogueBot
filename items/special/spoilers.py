import random

name = 'Мешочек со спойлерами'

description = (
	'Не вскрывать!'
)

price = 300
fightable = True
disposable = True

def fight_use(user, reply, room):
	reply('Ты бросаешь мешочек со спойлерами в врага и..')

	if random.random() < 0.66 or room.code_name == 'doctor_who':
		reply('Ничего не происходит.')
		reply('К сожалению, противник тщательно готовился к бою и досмотрел все сериалы.')
	else:
		reply('Ты — отвратительный человек. Но спойлеры подействовали: противник сбежал, закрыв глаза и уши!')
		user.won(reply)

	return 0
