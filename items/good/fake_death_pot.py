import random
from constants import *

name = 'Зелье полусмерти'

description = (
	'Читал «Ромео и Джульетта»? Вот эта штука поможет прbтвориться мертвым'
)

price = 100
shop_count = 2

disposable = True

fightable = True
def fight_use(user, reply, room):
	if random.random() > 0.5:
		reply('Ты успешно притворился мертвым и монстр ушел')
		user.leave(reply)
	else:
		reply('То ли монстр не поверил твоей игре, то ли наоборот: ты слишком убедительно притворялся, но факт остается фактом. Очнулся ты уже мертвым.')
		user.death(reply, reason=name)

	return 0