name = 'Дверь'

actions = [ 'Постоять', 'Открыть' ]

def get_actions(user):
	return actions

def enter(user, reply):
	reply('Дубовая!', photo='BQADAgAD9wgAAmrZzgfQsNScN9T3LwI')
	user.set_room_temp('cnt', 0)

def action(user, reply, text):
	if text == actions[0]:
		cnt = user.get_room_temp('cnt', def_val=0)
		if cnt > 10:
			reply('_Ты устал_')
		elif cnt > 20:
			reply('_Ты умер от изнеможения')
			user.death(reply, reason='Столкновение с дверью')
		reply('_тишина_')
		user.set_room_temp('cnt', cnt+1)
	else:
		reply('Ты открываешь дверь, а за ней... Коридор!')
		user.leave(reply)