name = 'Удача'

def enter(user, reply):
	reply('Открывая очередную дверь, ты споткнулся о порог и упал головой на острый пол. _Поражены вашей неудачей_')
	reply('В агониях вы укатились обратно в коридор. Так держать!', photo='BQADAgAD1wgAAmrZzgdfyW7V73sUzQI')
	user.make_damage(0, 25, reply, name='Порог')
	user.leave(reply)

def get_actions(user):
	return [ ]


def action(user, reply, text):
	user.leave(reply)