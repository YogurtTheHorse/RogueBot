name = 'Волшебная палочка'
description = (
	'Говорят, что каждая палочка сама выбирает хозяина, но чхал я на это. Можно делать «_Авада Кедавра!_» и убивать *всё*.'
)

price = 100

fightable = True
disposable = True
def fight_use(user, reply, room):
	reply('Авада Кедавра!\n\nПалочка убила всё вокруг и не только.')
	user.death(reply, reason='Магия')

	return 0