from localizations import locale_manager
name = locale_manager.get('items.good.fork.phrase_1')
description = (
  locale_manager.get('items.good.fork.phrase_2')
)

price = 150

fightable = True
disposable = True

def fight_use(user, reply, room):
  return 15
  reply(locale_manager.get('items.good.fork.phrase_3'))
