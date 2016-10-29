import random
import usermanager
from constants import *

BOLDNESS = '[Дерзновение]'
I_GROW_THERE = 'Я здесь родился и вырос. Мой дед открывал двери, мой отец открывал двери, и я открываю двери.'

SORRY = '—Извините, я погорячился.'
SHAME_ON_YOU = '—Только посмотри, в кого ты превратился! Ленность, чревоугодие!'

PLEASE = '—Ну Гееейб... плез :’('
OKAY = '—Ну и ладно, сам справлюсь!'

HOW_ARE_YOU = '—Как поживаете?'

name = 'Человек'

def enter(user, reply):
	msg = (
		'—Проходи, {0}, чего хотел?\n\nНа негнущихся коленях ты проходишь '
		'в середину комнаты. Да, глаза не подвели, это действительно...\n\n'
		'*Гейб Ньюэл*!'
	)
	reply(msg.format(user.name))
	user.set_room_temp('question', 'first')

	gabe_quest = user.get_variable('gabe', def_val=0)
	if user.has_item('chicken') and gabe_quest > 0:
		reply('—Где-то я уже Вас видел...')
		user.set_room_temp('question', 'chicken')


def action(user, reply, text):
	question = user.get_room_temp('question', def_val='first')
	gabe_quest = user.get_variable('gabe', def_val=0)

	if question == 'first':
		if gabe_quest == 2:
			reply('—О, {0}, привет, дружище! Давно не виделись! Прекрасно себя чувствую. Как сам?'.format(user.name))
			user.set_room_temp('question', 'howareyou')
		else:
			reply(
				'Ах, юноша, сколько я уже повидал искателей приключений в этой '
				'комнате. И все спрашивают одно и то же. Скажи мне лучше, почему '
				'ты изо дня в день открываешь двери? За ними нет того, кто бы '
				'поддержал тебя, проникся к тебе тёплыми чувствами. Там лишь те, '
				'кто желают тебе зла, совершенно омерзительные личности '
				'отвратительные создания.'
			)
			user.set_room_temp('question', 'second')
	elif question == 'second':
		if text == BOLDNESS:
			reply(
				'—Я вижу, Вы тут хорошо себя чувствуете, сидите, мудрствуете. '
				'За моими дверями всегда что-то новое, приключения и азарт '
				'битвы. А в этой, пропахшей клопами, комнате лишь четыре стены '
				'и изредка появляющиеся зеваки. Моё положение меня полностью '
				'устраивает. И кому из нас хуже?\n\nГейб Ньюэлл не ожидал '
				'такого напора, его глаза округлились, но он взял себя в руки:'
				'\n\n—Каждый может быть учтив с королем, но нужно быть '
				'джентльменом, чтобы учтиво вести себя с нищим. Я был вежлив, '
				'но ты отплатил мне грубостью. '
			)
			user.set_room_temp('question', 'boldness')
		else:
			reply(
				'—Неужели тебя не пугает эта перспектива? Всю жизнь открывать '
				'эти чёртовы двери. Разве не хочется тебе увидеть что-то '
				'новое в жизни, кроме этих Магов, Оборотней и прочих гадов?'
			)
			user.set_room_temp('question', 'grow')
	elif question == 'boldness':
		if text == SHAME_ON_YOU:
			reply('—Что ж, ступай.\n\nВ этой комнате вы нашли:\nVAC бан', photo='BQADAgAD4ggAAmrZzgd0WYobKpDxOAI')
			user.death(reply, reason='VAC бан')
		else:
			reply('—Ничего, с каждым может случиться. ')
			reply('Ты оснозал, что ты был неправ и ушел')

			user.leave(reply)
	elif question == 'grow':
		reply('—Возможно и есть, но если это так, я тебе об этом ничего не скажу. Ты же не любишь спойлеры? ;)')
		user.set_room_temp('question', 'question')
	elif question == 'question':
		if text == PLEASE:
			reply(
				'—Ну ладно, я дам подсказку. Но с тебя причитается. Заходи '
				'сюда же через пару часов, меня сменит господин Кодзима. '
				'Может быть, он расскажет тебе что-нибудь по этой теме. '
				'А может и нет. И помни, если тебе удастся отсюда выбраться, '
				'принеси мне пожалуйста жареную курочку. Сто лет её не ел, '
				'я тебя *очень щедро отблагодарю*!'
			)
		else:
			reply(
				'—Молодец, хвалю за любознательность! Но помни, если тебе '
				'удастся отсюда выбраться, принеси мне пожалуйста жареную '
				'курочку. Сто лет её не ел, я тебя *очень щедро отблагодарю*!'
			)
		user.leave(reply)
		user.set_variable('gabe', 1)
	elif question == 'howareyou':
		reply('Вы мило побеседовали.')
		user.leave(reply)
	elif question == 'chicken':
		reply('—Глазам не верю! Настоящая! Ароматная! Мой спаситель.')
		user.set_room_temp('question', 'smile')
	elif question == 'smile':
		reply(
			'Кажется у Гейба начали блестеть глаза.\n—Я обещал хорошую награду'
			'. Вот, 1 000 золота, ни в чём себе не отказывай. Если будут '
			'проблемы — обращайся в любое время.'
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
			ans = [ '—Это правда Вы?', '—А можно автограф?' ]
			if user.get_charisma() > 10:
				ans.append('—А когда третья Half-Life выйдет?')
		else:
			ans = [ HOW_ARE_YOU ]
	elif question == 'chicken':
		ans = [ '—Это же я, {0}!\n Принёс курочку, берите, пока горячая.'.format(user.name) ]
	elif question == 'howareyou':
		ans = [ '—Крошу мобов пачками!' ]
	elif question == 'second':
		ans = [ BOLDNESS, I_GROW_THERE ]
	elif question == 'boldness':
		ans = [ SORRY, SHAME_ON_YOU ]
	elif question == 'grow':
		ans = [ 'Разве у меня есть выбор?' ]
	elif question == 'question':
		ans = [ PLEASE, OKAY ]
	elif question == 'smile':
		ans = [ '(глупо улыбаться и наслаждаться чувством собственной важности)' ]
	else:
		ans = [ 'Загрузка' ]

	return ans