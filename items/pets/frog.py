from localizations import locale_manager
from localizations import locale_manager
name = locale_manager.get('items.pets.frog.phrase_1')
description = locale_manager.get('items.pets.frog.phrase_2')
price = 0


def on_room(user, reply, room):
	msg = locale_manager.get('items.pets.frog.phrase_3')
	pet_name = user.get_pet().real_name

	reply(msg.format(pet_name), photo='BQADAgADFwAD0lqIATqAWnECKZjoAg')
