import random

name = 'Звонок гейбу'

description = (
	'Решит любые проблемы.'
)

price = 300
fightable = True
disposable = True

def fight_use(user, reply, room):
	reply('Идут гудки..')

	reply('—Алло, Гейб, у меня тут проблемы с монстром.\n—Каким монстром?\b\nДействительно, каким? Твой противник сбежал.')
	user.won(reply)

	return 0
