from localizations import locale_manager
import random

name = locale_manager.get('rooms.default.boss.moonlight_butterfly.phrase_1')

hp = 49500
damage_range = ( 0, 49 )

coins = random.randrange( 1000, 21000, 1 )


def skill_preparing(user, reply, boss):
  msg = (
    locale_manager.get('rooms.default.boss.moonlight_butterfly.phrase_2')
  )

  reply(msg, photo='BQADAgAD-wgAAmrZzgcvl-cLwNrVkgI')
