import random

name = 'Мешочек со спойлерами'

description = (
	'Не вскрывать!'
)

price = 300
fightable = True
disposable = True


def can_use(user, reply, room):
  reply('Ты бросаешь мешочек со спойлерами в врага и...')

  return random.random() > 0.66 and room.code_name != 'doctor_who' and room.room_type != 'boss'


def success(user, reply, room):
  reply('Ты — отвратительный человек. Но спойлеры подействовали: противник сбежал, закрыв глаза и уши!')
  user.won(reply)


def failure(user, reply, room):
  reply('Ничего не происходит.')
  reply('К сожалению, противник тщательно готовился к бою и досмотрел все сериалы.')
