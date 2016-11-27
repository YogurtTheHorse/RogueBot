from localizations import locale_manager
import random

name = locale_manager.get('rooms.default.boss.cthulhu.phrase_1')

hp = 575900
damage_range = ( 150, 250 )

coins = random.randrange( 1000, 251000, 1 )


def skill_preparing(user, reply, boss):
  msg = (
    locale_manager.get('rooms.default.boss.cthulhu.phrase_2')
  )

  reply(msg, photo='BQADAgAD_AgAAmrZzge-xwd2a6LXzAI')


def on_die(user, reply):
	msg = (
		locale_manager.get('rooms.default.boss.cthulhu.phrase_3'))

	reply(msg)
