from random import randrange

name = 'Василиск'

hp = 135
damage_range =  ( 16, 25 )

coins = randrange(100, 150, 5)

loot = [ 'tooth_basilisk' ]


def enter(user, reply):
	msg = (
		'Дверь открывается, и ты попадешь в длинную залу со множеством ответвлений.\n'
		'Знакомый интерьер. Не Находишь?\n'
		'Хм, что это там за движение впереди?\n'
		'Госпади! Да это же _ВАСИЛИСК_!!!\n')
	reply(msg)
