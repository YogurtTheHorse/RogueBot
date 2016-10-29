import databasemanager
import tornamentmanager

name = 'Цезарь'

actions = [ 'Записаться', 'Уйти' ]

def get_actions(user):
	return actions

def enter(user, reply):
	reply('Перед тобой стоит Цезарь. Он рассказал тебе о гладиаторских боях и предложил тебе учавствовать.')
	reply(
		'Если ты запишешься на турнир то в любой момент игры твоего '
		'персонажа может телепортиртировать в _Колизей_ лично богом войны Марсом. '
		'Скорее всего, ты будешь там не один и тебе придется драться с остальными игроками.'
		'Победитель получит достойные *призы*, а остальные — *смерть*.',
		photo='BQADAgADTgkAAmrZzgdMf1IntNiY4wI'
	)

def action(user, reply, text):
	if text == actions[0]:
		if user.get_damage() > 100:
			reply('Ты слишком силен для всего этого, я не могу пустить тебя к ним.')
		elif databasemanager.get_variable('ces', def_val=False) is False:
			reply('На сегодня запись закрыта. Приходите завтра.')
		else:
			reply('Тебе сообщат о начале турнира.')
			if tornamentmanager.add_to_list('cesar', user.uid) < 0:
				reply('Подожди-ка... Ты уже в списках')
	else:
		reply('Так и быть. Ступай')
	user.leave(reply)
