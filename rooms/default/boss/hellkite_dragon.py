import random

name = 'Красная Виверна'

hp = 175500
damage_range = ( 0, 175 )

coins = random.randrange( 1000, 71000, 1 )


def skill_preparing(user, reply, boss):
  msg = (
    'Ты услышал громыхающее рычание и увидел, что Красная Виверна готовится выпустить в тебя огромный поток пламени.'
  )

  reply(msg)
