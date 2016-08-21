from constants import *

name = 'Учитель Японского!'

room_type = 'other'

# 			Выучить японский, Сказать, что уже знаешь
actions = [ '日本語を学びます', 'すでに日本語を知っていると言うこと' ]

def get_actions(user):
	return actions

def dice(user, reply, result, subject=None):
	if result > DICE_MIDDLE:
		reply('Неплохо, но у Толи слишком мало клиентов, чтобы еще и платить несостоявшимся искателям приключений, поэтому пойдем поищем чего еще')
	else:
		reply('Мда. Тебя избили битой за то, что ты сломал ножницы.')

		if user.has_item('scissors'):
			user.remove_items_with_tag('scissors')
			reply('О. Так у тебя есть ножницы. Ну и их отберем!')

		user.make_damage(20, 30, reply)
	user.leave(reply)

def enter(user, reply):
	reply('ようこそ！\n私はトトロです')

def action(user, reply, text):
	if text == actions[0]:		
		if user.paid(50):
			reply('Теперь ты знаешь японский! おめでとうございます!')

			user.add_tag(JAPANESE)
		else:
			reply('У тебя не хватило денег, чтобы выучить японский, но зато у тебя теперь есть сюриукен и головная боль')
			user.make_damage(20, 30, reply)
		
		user.leave(reply)
	elif text == actions[1]:
		if user.has_tag(JAPANESE):
			reply('そう。\nМастер попрощался с тобой')
			user.leave(reply)
		else:
			reply('私はトトロです')
	else:
		reply('私はトトロです')
