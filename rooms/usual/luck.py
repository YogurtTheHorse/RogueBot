name = 'Удача'

def enter(user, reply):
	reply('Открывая очередную дверь вы споткнулись о порог и упали головой на острый камень. Паражены вашей неудачей')
	reply('В агониях вы укатились обратно в коридор. Так держать!')
	user.make_damage(0, 25, reply, name='Порог')
	user.leave(reply)

def get_actions(user):
	return х ъ


def action(user, reply, text):
	user.leave(reply)