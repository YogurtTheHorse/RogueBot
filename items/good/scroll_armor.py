from constants import *
from utils.buffs import ScrollBuff_armor
import random

name = 'Свиток черепахи'

description = (
	'Свиток железный, его не согнуть'
)

price = 100

fightable = True
disposable = True

def fight_use(user, reply, room):
	if user.use_mana(50):
		reply('Ты читаешь заклинание и твои руки начинают трястись.\nТы не в состоянии их больше сдерживать\nОни начинают описывать круги. Твоя броня увеличилась на 1000 очков.')
		user.new_buff(ScrollBuff_armor())
	else:
		reply('Недостаточно маны')
		user.add_item('good', 'scroll_armor')
	return 0
