from constants import QUINQUEPEDE_STICKER

name = 'Неестественная семилапка'

hp = 50
damage_range =  ( 15, 30 )

coins = 30

loot = [ ]

def enter(user, reply):
	reply('Семилапая ящерица, чудный эксперимент магов по одомашниванию драконов.', photo=QUINQUEPEDE_STICKER)
