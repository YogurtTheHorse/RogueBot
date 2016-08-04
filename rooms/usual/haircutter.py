from constants import *

name = 'Парикмахерская'

room_type = 'other'
actions = [ 'Подстричься за 10 золотых', 'Сказать, что ты парикмахер и попробовать устроиться на работу', 'Сделать вид, что ошибся дверью' ]

def get_actions(user):
	return actions

def dice(user, reply, result, subject=None):
	if result > DICE_MIDDLE:
		reply('Неплохо, но у Толи слишком мало клиентов, чтобы еще и платить несостоявшимся искателям приключений, поэтому пойдем поищем чего еще')
	else:
		reply('Мда. Тебя избили битой за то, что ты сломал ножницы.')
		user.make_damage(20, 30)
	user.leave(reply)

def enter(user, reply):
	msg = (
		'Добро пожаловать в парикмахерскую Дяди Толи!\n'
		'Мы здесь вне конкуренции — конкурировать не с чем.'
	)
	reply(msg)

def action(user, reply, text):
	if text == actions[0]:
		user.remove_items_with_tag('hair')
		
		if user.paid(10):
			reply('С вами приятно работать!')
		else:
			reply('Наверное, без денег лучше не стричься. Вам постригли волосы и не только.')
			user.make_damage(20, 30)
		
		user.leave(reply)
	elif text == actions[1]:
		reply('Ну покажи на что способен')
		user.throw_dice(reply)
	else:
		user.leave(reply)
