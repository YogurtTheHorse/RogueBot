from localizations import locale_manager
import random

name = locale_manager.get('rooms.default.boss.black_knight.phrase_1')

hp = 129500
damage_range = ( 0, 129 )

coins = random.randrange( 1000, 51000, 1 )


def skill_preparing(user, reply, boss):
  msg = (
    locale_manager.get('rooms.default.boss.black_knight.phrase_2')
  )

  reply(msg, photo='BQADAgADBQkAAmrZzgfwyyrSjVn2rgI')
