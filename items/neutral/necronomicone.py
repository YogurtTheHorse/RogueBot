name = 'Некрономикон'
description = 'Тяжелая книга, сделанная из кожи. Кажется из человеческой кожи. Открыв ее ты видишь странные символы, написанные кровью. От них у тебя начинает болеть голова.'
price = 600

disposable = True
usable = True
def on_use(user, reply):
	if user.has_item('puzzle'):
		reply('Ты видишь странных существ, но между тобой и этими существами словно стена. Их время еще не пришло...')
	else:
		user.open_room(reply, 'special', 'the_thing_from_below')