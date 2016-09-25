from constants import *

name = '先生'

room_type = 'other'

def get_actions(user):
	if user.has_tag(JAPANESE):
		return [ 'Выучить японский', 'Сказать, что уже знаешь', 'Молча стоять' ]
	else:
		return [ '日本語を学びます', 'すでに日本語を知っていると言うこと', '静かに立ちます' ]

def enter(user, reply):
	if user.has_tag(JAPANESE):
		reply('Привет!')
	else:
		reply('ようこそ！\n私はトトロです')

def action(user, reply, text):
	if text == get_actions(user)[0]:		
		if user.paid(50):
			reply('Теперь ты знаешь японский! おめでとうございます!')

			user.add_tag(JAPANESE)
		else:
			reply('У тебя не хватило денег, чтобы выучить японский, но зато у тебя теперь есть сюрикен и головная боль.')
			user.make_damage(20, 30, reply, death=False)
		
		user.leave(reply)
	elif text == get_actions(user)[1]:
		if user.has_tag(JAPANESE):
			reply('Мастер попрощался с тобой')
			user.leave(reply)
		else:
			reply('私はトトロです')
	else:
		if user.has_tag(JAPANESE):
			reply('Я — сенсей!')
		else:
			reply('私はトトロです')
