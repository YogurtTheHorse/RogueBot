import random

name = 'Свиток вспышки'

description = (
	'Вспыхивает всё вокруг.\n'
	'Надпись на обороте: применять осторожно.'
)

price = 9990
fightable = True
disposable = True


def success(user, reply, room):
	msg = (
		'Яркий свет ослепил всех вокруг, '
		'у тебя появилась возможность убежать и ты убежал!'
	)

	reply(msg)


	if user.gold > 0:
		msg = (
			'Ты бежал насколько быстро, что растряс все свои денежки.\n'
			'Ты потерял {}.'
		)

		coins = user.gold // 2

		user.steal(coins)

		reply(msg.format(coins))

	user_items = user.get_items()

	item = random.choice(user_items)

	if user_items and item.name is not name:
		msg = (
			'А еще ты потерял {}'
		)

		user.remove_item_by_name(item.name)

		reply(msg.format(item.name))

	user.leave(reply)