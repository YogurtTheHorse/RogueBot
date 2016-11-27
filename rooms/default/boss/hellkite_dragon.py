from localizations import locale_manager
import random

name = locale_manager.get('rooms.default.boss.hellkite_dragon.phrase_1')

hp = 175500
damage_range = ( 0, 175 )

coins = random.randrange( 1000, 71000, 1 )


def skill_preparing(user, reply, boss):
  msg = (
    locale_manager.get('rooms.default.boss.hellkite_dragon.phrase_2')
  )

  reply(msg)
