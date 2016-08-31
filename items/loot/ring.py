name = 'Кольцо'

description = (
	'… И в это кольцо он засадил всю свою жестокость,\n'
	'злобу свою засадил, детские комплексы,\n'
	'ну там привычки нехорошие и всё такое…\n'
)

price = 0
iscursed = True


def on_room(user, reply, room):
	reply('Опять вставило, да?')
	user.make_damage(10, 20, reply, death=False)
