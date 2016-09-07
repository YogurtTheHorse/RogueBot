import random

name = 'Звонок гейбу'

description = (
	'Решит любые проблемы.'
)

price = 300
fightable = True
disposable = True


def can_use(user, reply, room):
  msg = (
    'Идут гудки..\n'
    '—Алло, Гейб, у меня тут проблемы с монстром.\n'
    '—Каким монстром?\b'
  )

  reply(msg)

  return room.room_type != 'boss'


def success(user, reply, room):
  msg = (
    'Действительно, каким? Твой противник сбежал.'
  )

  reply(msg)
  user.won(reply)


def failure(user, reply, room):
  msg = (
    '—*Ахххр-гр!*\n'
    'Гейб услышал рык монстра и повесил трубку.'
  )

  reply(msg)
