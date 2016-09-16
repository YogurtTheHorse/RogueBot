from utils.buffs import Buff

name = 'Золотой песок'
price = 700
description = (
	'Увеличивает получаемое золото в два раза!'
)

usable = True
disposable = True

def on_use(user, reply):
	reply('Пыщ-пыщ.')

	has_gold_buff = False

	for b in user.buffs:
		if b.get_name() == 'gold':
			has_gold_buff = True
			break
	
	gold_bonus = 2
	if has_gold_buff:
		gold_bonus = 0
		reply('Ой, подождите-ка... У тебя песок попал в глаза и ты не видишь золото в этом блеске. Как жаль :(')

	bf = Buff(10, name='gold', gold_bonus=gold_bonus)

	user.new_buff(bf)
