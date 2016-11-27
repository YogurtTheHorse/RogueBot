from localizations import locale_manager
import random
import usermanager
from constants import *

BOLDNESS = '[Дерзновение]'
I_GROW_THERE = locale_manager.get('rooms.default.special.gabe.phrase_8')

SORRY = locale_manager.get('rooms.default.special.gabe.phrase_9')
SHAME_ON_YOU = locale_manager.get('rooms.default.special.gabe.phrase_10')

PLEASE = '—Ну Гееейб... плез :’('
OKAY = locale_manager.get('rooms.default.special.gabe.phrase_11')

HOW_ARE_YOU = locale_manager.get('rooms.default.special.gabe.phrase_12')

name = locale_manager.get('rooms.default.special.gabe.phrase_13')

def enter(user, reply):
	msg = (
		locale_manager.get('rooms.default.special.gabe.phrase_1')
	)
	reply(msg.format(user.name))
	user.set_room_temp('question', 'first')

	gabe_quest = user.get_variable('gabe', def_val=0)
	if user.has_item('chicken') and gabe_quest > 0:
		reply(locale_manager.get('rooms.default.special.gabe.phrase_14'))
		user.set_room_temp('question', 'chicken')


def action(user, reply, text):
	question = user.get_room_temp('question', def_val='first')
	gabe_quest = user.get_variable('gabe', def_val=0)

	if question == 'first':
		if gabe_quest == 2:
			reply(locale_manager.get('rooms.default.special.gabe.phrase_15').format(user.name))
			user.set_room_temp('question', 'howareyou')
		else:
			reply(
				locale_manager.get('rooms.default.special.gabe.phrase_2'))
			user.set_room_temp('question', 'second')
	elif question == 'second':
		if text == BOLDNESS:
			reply(
				locale_manager.get('rooms.default.special.gabe.phrase_3') + locale_manager.get('rooms.default.special.gabe.phrase_4'))
			user.set_room_temp('question', 'boldness')
		else:
			reply(
				locale_manager.get('rooms.default.special.gabe.phrase_5'))
			user.set_room_temp('question', 'grow')
	elif question == 'boldness':
		if text == SHAME_ON_YOU:
			reply('—Что ж, ступай.\n\nВ этой комнате вы нашли:\nVAC бан', photo='BQADAgAD4ggAAmrZzgd0WYobKpDxOAI')
			user.death(reply, reason='VAC бан')
		else:
			reply(locale_manager.get('rooms.default.special.gabe.phrase_16'))
			reply(locale_manager.get('rooms.default.special.gabe.phrase_17'))

			user.leave(reply)
	elif question == 'grow':
		reply('—Возможно и есть, но если это так, я тебе об этом ничего не скажу. Ты же не любишь спойлеры? ;)')
		user.set_room_temp('question', 'question')
	elif question == 'question':
		if text == PLEASE:
			reply(
				locale_manager.get('rooms.default.special.gabe.phrase_6'))
		else:
			reply(
				locale_manager.get('rooms.default.special.gabe.phrase_7'))
		user.leave(reply)
		user.set_variable('gabe', 1)
	elif question == 'howareyou':
		reply(locale_manager.get('rooms.default.special.gabe.phrase_18'))
		user.leave(reply)
	elif question == 'chicken':
		reply(locale_manager.get('rooms.default.special.gabe.phrase_19'))
		user.set_room_temp('question', 'smile')
	elif question == 'smile':
		reply(
			locale_manager.get('rooms.default.special.gabe.phrase_20')
		)
		user.add_item('special', 'call_gabe')
		user.remove_item('chicken')
		user.set_variable('gabe', 2)
		
		user.leave(reply)



def get_actions(user):
	question = user.get_room_temp('question', def_val='first')
	gabe_quest = user.get_variable('gabe', def_val=0)
	ans = [ ]

	if question == 'first':
		if gabe_quest != 2:
			ans = [ locale_manager.get('rooms.default.special.gabe.phrase_22'), locale_manager.get('rooms.default.special.gabe.phrase_23') ]
			if user.get_charisma() > 10:
				ans.append('—А когда третья Half-Life выйдет?')
		else:
			ans = [ HOW_ARE_YOU ]
	elif question == 'chicken':
		ans = [ locale_manager.get('rooms.default.special.gabe.phrase_24').format(user.name) ]
	elif question == 'howareyou':
		ans = [ locale_manager.get('rooms.default.special.gabe.phrase_25') ]
	elif question == 'second':
		ans = [ BOLDNESS, I_GROW_THERE ]
	elif question == 'boldness':
		ans = [ SORRY, SHAME_ON_YOU ]
	elif question == 'grow':
		ans = [ locale_manager.get('rooms.default.special.gabe.phrase_26') ]
	elif question == 'question':
		ans = [ PLEASE, OKAY ]
	elif question == 'smile':
		ans = [ '(глупо улыбаться и наслаждаться чувством собственной важности)' ]
	else:
		ans = [ locale_manager.get('rooms.default.special.gabe.phrase_27') ]

	return ans