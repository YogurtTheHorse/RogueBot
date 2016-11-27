from localizations import locale_manager
import random

name = locale_manager.get('rooms.default.boss.naping_dragon.phrase_1')

hp = 77500
damage_range = ( 0, 77 )

coins = random.randrange( 1000, 31000, 1 )


def skill_preparing(user, reply, boss):
  msg = (
    locale_manager.get('rooms.default.boss.naping_dragon.phrase_2')
  )

  reply(msg)
