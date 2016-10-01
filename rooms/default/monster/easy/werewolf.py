from constants import WOLF_STICKER

name = 'Волк-оборотень'

hp = 35
damage_range =  ( 15, 23 )

coins = 21

loot = [ ]


def enter(user, reply):
	reply('Чудовищное волкоподобное существо!', photo=WOLF_STICKER)
