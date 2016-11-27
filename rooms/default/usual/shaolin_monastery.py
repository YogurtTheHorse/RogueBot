from localizations import locale_manager
from constants import *

name = locale_manager.get('rooms.default.usual.shaolin_monastery.phrase_1')

room_type = 'other'

def get_actions(user):
	return [ locale_manager.get('rooms.default.usual.shaolin_monastery.phrase_2'), locale_manager.get('rooms.default.usual.shaolin_monastery.phrase_3'), locale_manager.get('rooms.default.usual.shaolin_monastery.phrase_4')]

def enter(user, reply):
	reply(locale_manager.get('rooms.default.usual.shaolin_monastery.phrase_5'), photo='BQADAgADFQkAAmrZzgeH6hmh7PbRYgI')

def action(user, reply, text):
	actions = get_actions(user)

	if text == actions[0]:
		user.throw_dice(reply, 'fragile')
	elif text == actions[1]:
		user.defence += 5
		reply('Ты принял участие в тренировке монахов, теперь твоё тело крепче. Это стоило тебе добровольного пожертвования.', photo='BQADAgADFAkAAmrZzgfPUvv4wiphMQI')
		if not user.paid(50):
			reply(locale_manager.get('rooms.default.usual.shaolin_monastery.phrase_6'))
			user.make_damage(20, 60, reply, name=name)
		user.leave(reply)
	else:
		if user.has_item('tin_foil_hat'):
			reply(' — Странные у тебя методы защиты, друг. Но если тебе этот блестящий конус на голове помогает, то носи конечно.')
		user.throw_dice(reply, 'escape')

def dice(user, reply, result, subject=None):
	if subject == 'fragile':
		if result > DICE_MIDDLE:
			reply(' — Неплохо, но ведь нет предела совершенству? Приходи еще, потренируемся.')
			user.leave(reply)
		else:
			reply(' — Маловато, конечно, но жить можно.\nДай-ка я тебе пару приёмов покажу. Ой...')
			user.make_damage(50, 80, reply, name=name)
			user.leave(reply)
	elif subject == 'escape':
		if result > (DICE_MAX / 4) * 3:
			reply(' — Да осветит солнце путь твой.')
			user.leave(reply)
		else:
			reply('— Как ты вообще с таким подходом к жизни живешь? Парни, его надо потренировать.\n\n — Ну кто же знал что ты такой хрупкий.')
			user.make_damage(50, 80, reply, name=name)
			user.leave(reply)	
