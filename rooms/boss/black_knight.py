import random

name = 'Чёрный Рыцарь'

hp = 129500
damage_range = ( 0, 129 )

coins = random.randrange( 1000, 51000, 1 )


def skill_preparing(user, reply, boss):
  msg = (
    'Ты слышишь грохот и рычание. Черный Рыцарь готовится проткнуть тебя своим клинком.'
  )

  reply(msg)
