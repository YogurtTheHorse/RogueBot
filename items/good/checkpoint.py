name = 'Свиток сохранения'
description = 'Сохрани меня!'
price = 10000

usable = True

def on_use(user, reply):
	user.remove_item('checkpoint')
	reply('Вы сохранены!')
	user.save()