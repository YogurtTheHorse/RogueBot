from localizations import locale_manager
import random

name = locale_manager.get('items.special.call_gabe.phrase_3')

description = (
	locale_manager.get('items.special.call_gabe.phrase_4')
)

price = 300
fightable = True
disposable = True


def can_use(user, reply, room):
  msg = (
    locale_manager.get('items.special.call_gabe.phrase_1'))

  reply(msg)

  return room.room_type != 'boss'


def success(user, reply, room):
  msg = (
    locale_manager.get('items.special.call_gabe.phrase_5')
  )

  reply(msg)
  user.won(reply)


def failure(user, reply, room):
  msg = (
    locale_manager.get('items.special.call_gabe.phrase_2'))

  reply(msg)
