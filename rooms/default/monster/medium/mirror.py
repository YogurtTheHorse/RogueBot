from utils import costumes

from constants import *

name = 'Зеркало'

hp = 1
element = NONE
damage_range =  ( 0, 0 )

coins = 200

loot = [ ]

def enter(user, reply):
	msg = (
		'Ты видишь что-то странное в костюме {0}.'.format(costumes.get_costume(user.costume)['who'])
	)
	reply(msg, photo='BQADAgAD2ggAAmrZzgeHYxYQWFaEZgI')

	user.set_room_temp('hp', user.hp)

	ch = user.get_charisma()

	if ch < 0:
		reply('Оно треснуло.')
		user.won(reply)
	elif ch > 15:
		reply('Такой красивый. Иди с миром ;)')
		user.won(reply)

def make_damage(user, reply, dmg):
	hp = user.get_room_temp('hp', 0)
	hp -= dmg + 1

	if hp <= 0:
		user.won(reply)

		reply('Ты перестарался и оно нанесло тебе немного урона в ответ.')

		user.make_damage(0, -hp, reply, defence=False, name=name)
	else:
		user.set_room_temp('hp', hp)

		reply('Ты нанес сам себе урон, равный *{0}*'.format(dmg))
		user.make_damage(dmg, dmg, reply, defence=False, name=name)
