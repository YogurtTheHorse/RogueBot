import random

name = 'Разверстый Дракон'

hp = 77500
damage_range = ( 0, 77 )

coins = random.randrange( 1000, 31000, 1 )


def skill_preparing(user, reply, boss):
  msg = (
    'Ты услышал громыхающее рычание и увидел, что Разверстый Дракон взлетает ввысь и вот-вот обрушится на тебя.'
  )

  reply(msg)
