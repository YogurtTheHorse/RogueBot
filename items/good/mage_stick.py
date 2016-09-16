name = 'Посох начинающего мага'
description = (
	'Посох мага. Увеличивает твой магический урон. Круто, да?\n'
	'Только осторожно, он хрупкий.'
)

price = 100
mana_damage = 20
fightable = True

def fight_use(user, reply, room):
	reply('Ты сломал свой посох, но зато у кого-то теперь шишка.')

	user.remove_item_by_name(name)

	return 5