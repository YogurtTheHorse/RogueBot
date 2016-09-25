name = 'Вилка'
description = (
  'Один удар, три дырки.'
)

price = 150

fightable = True
disposable = True

def fight_use(user, reply, room):
  return 15
  reply('Вилка сломалась.')
