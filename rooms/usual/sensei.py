from constants import *

name = '先生'

room_type = 'other'

# 			Выучить японский, Сказать, что уже знаешь,  Молча стоять
actions = [ '日本語を学びます', 'すでに日本語を知っていると言うこと', '静かに立ちます' ]

def get_actions(user):
	return actions

def enter(user, reply):
	reply('ようこそ！\n私はトトロです')

def action(user, reply, text):
	if text == actions[0]:		
		if user.paid(50):
			reply('Теперь ты знаешь японский! おめでとうございます!')

			user.add_tag(JAPANESE)
		else:
			reply('У тебя не хватило денег, чтобы выучить японский, но зато у тебя теперь есть сюрикен и головная боль.')
			user.make_damage(20, 30, reply, death=False)
		
		user.leave(reply)
	elif text == actions[1]:
		if user.has_tag(JAPANESE):
			reply('そう。\nМастер попрощался с тобой')
			user.leave(reply)
		else:
			reply('私はトトロです')
	else:
		reply('私はトトロです')
