name = 'Мазь "Звёздочка"'
description = 'Лечебная мазь универсального действия. Кажется, может вылечить даже от рака.'
price = 300

usable = True
disposable = True

def on_use(user, reply):
	reply('Вот так-то лучше!')

	user.heal(25)

	user.buffs = [ b for b in user.buffs if not b.is_negative() ]