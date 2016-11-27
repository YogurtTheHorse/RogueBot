from localizations import locale_manager
from time import time
from constants import *

INJURED = 'injured'

name = 'Потрёпанный мужик с дробовиком'

GO = locale_manager.get('rooms.default.usual.no_sudden_movement.phrase_1')
WAIT = locale_manager.get('rooms.default.usual.no_sudden_movement.phrase_2')

DELTA_TIME_MAX = 15

def get_actions(user):
	return [ GO, WAIT ]

def enter(user, reply):
	reply('— Ты еще кто такой?! Не дергайся, дай мне проверить твои документы! У меня на это уйдёт примерно 15 секунд.', photo='BQADAgAD6QgAAmrZzgd8DgIPKNYJ7QI')

	user.set_room_temp('time', time())

def action(user, reply, text):
	t2 = time()
	delta = t2 - user.get_room_temp('time')

	if text == GO:
		if user.has_tag(INJURED) and delta < DELTA_TIME_MAX:
			reply('— Я тебя предупреждал!')
			user.death(reply, reason=locale_manager.get('rooms.default.usual.no_sudden_movement.phrase_3'))
		elif delta < DELTA_TIME_MAX:
			reply('— Я тебя предупреждаю последний раз.\nМужик поднимает дробовик и стреляет чуть правее твоей головы, но тебя все равно зацепило.\n*Click-Clack*\n— Следующий будет в голову.')
			user.add_tag(INJURED)
			user.make_damage(10, 30, reply, death=False, name=name)
		elif delta > DELTA_TIME_MAX:
			if user.has_tag(INJURED):
				user.remove_tag(INJURED)
			reply('— Вали отсюда! Быстро!')
			user.leave(reply)
	elif text == WAIT:
		if delta < DELTA_TIME_MAX:
			reply('В комнате очень тихо. Настолько что ты слышишь своё собственное сердцебиение.\nЕще бы его не услышать, ведь на вас направлен дробовик!')	
		else:
			reply(' — Иди!')
