import random

name = 'Лиса'
description = 'Оказывает поддержку в трудную минуту'
price = 0

MAX_MAGIC_POWER = 10


def on_room(user, reply, room):
	if room.room_type in [ 'monster', 'boss' ]:
		msg = (
			'Твой лис {} спрятался позади тебя.'
		)

		pet_name = user.get_pet().real_name

		reply(msg.format(pet_name))


def get_damage_bonus(user, reply):
	msg = (
		'Твой лис {} кастует заклинание.'
	)

	pet_name = user.get_pet().real_name

	user.add_tag('fox_magic')

	magic_power = user.tags.count('fox_magic')

	reply(msg.format(pet_name))


	if magic_power >= MAX_MAGIC_POWER or random.random() < 0.15:
		msg = (
			'Твой лис {} восстановил тебе *{}* HP.'
		)
		
		heal_hp = int(user.max_hp * (magic_power / 30))

		user.heal(heal_hp)
		user.remove_tags('fox_magic')

		reply(msg.format(pet_name, heal_hp))

	return 0