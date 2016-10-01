from constants import MINION_STICKER
from random import randrange

name = 'Миньон'
hp = 23
damage_range = ( 1, 4 )

coins = randrange(5, 10, 2)

loot = [ 'banana' ]


def enter(user, reply):
	reply(
		'Это странное желтое существо в очках разговаривает на каком-то странном диалекте.\n'
		'Минуточку, я посмотрю в своем справочнике.\n'
		'Тут написано что это Миньон.\n'
		'Очень интересно...',
		photo=MINION_STICKER
	)