import random

name = 'Черный Рыцарь'

hp = 129500
damage_range = ( 0, 129 )

coins = random.randrange( 1000, 51000, 1 )


def skill_preparing(user, reply, boss):
  msg = (
    'Ты услышал громыхающее рычание и увидел, что Черный Рыцарь готовится со всей силы выпустить в тебя свой клинок.'
  )

  reply(msg, photo='BQADAgADBQkAAmrZzgfwyyrSjVn2rgI')
