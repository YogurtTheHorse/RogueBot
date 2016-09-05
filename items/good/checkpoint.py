name = 'Свиток сохранения'
description = 'Сохрани меня!'
price = 10000

usable = True
disposable = True

def on_use(user, reply):
	reply('Вы сохранены!')
	user.save()