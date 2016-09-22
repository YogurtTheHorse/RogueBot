name = 'Лягушка'
description = 'Тычет вилкой'
price = 0


def on_room(user, reply, room):
	msg = '{} уже давно мертв от удара током, но главное — верить.'
	pet_name = user.get_pet().real_name

	reply(msg.format(pet_name), photo='BQADAgADFwAD0lqIATqAWnECKZjoAg')
