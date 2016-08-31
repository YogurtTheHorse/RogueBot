name = 'Яблоня'

actions = [ 'Взять', 'Отказаться' ]

def get_actions(user):
	return actions

def enter(user, reply):
	msg = (
		'Огромная яблоня растет посреди полянки с травкой и цветочками, '
		'голая девушка под яблоней предлагает яблочко. '
	)
	reply(msg)

def action(user, reply, text):
	if text == actions[0]:
		reply('Ты съедаешь яблоко, а девушка дает тебе езе одно в дорогу.')

		reply('В облаках загремел гром, девушку убило молнией. Ну ниего, тут таких еще куча. Спасибо, Господь!')

		user.hp = min(user.max_hp, user.hp + 50)
		user.add_item('loot', 'apple')
	else:
		reply('Из дерева выпадает змей и кусает тебя.')
		user.make_damage(20, 30, reply)

	user.leave(reply)
