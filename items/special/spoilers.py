from localizations import locale_manager
import random

name = locale_manager.get('items.special.spoilers.phrase_1')

description = (
	locale_manager.get('items.special.spoilers.phrase_2')
)

price = 300
fightable = True
disposable = True


def can_use(user, reply, room):
  reply(locale_manager.get('items.special.spoilers.phrase_3'))

  return random.random() > 0.66 and room.code_name != 'doctor_who' and room.room_type != 'boss'


def success(user, reply, room):
  reply(locale_manager.get('items.special.spoilers.phrase_4'))
  user.won(reply)


def failure(user, reply, room):
  reply(locale_manager.get('items.special.spoilers.phrase_5'))
  reply(locale_manager.get('items.special.spoilers.phrase_6'))
