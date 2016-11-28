from localizations import locale_manager
name = locale_manager.get('items.loot.dragon_sword.phrase_2')
description = (
	locale_manager.get('items.loot.dragon_sword.phrase_3')
)

price = 1000

fightable = True

def fight_use(user, reply, room):
	if room.code_name == 'dragon' or room.code_name == 'quinquepede':
		reply(locale_manager.get('items.loot.dragon_sword.phrase_4'))
		user.won(reply)

		return 0
	else:
		msg = (
			locale_manager.get('items.loot.dragon_sword.phrase_1'))
		reply(msg)

		user.make_damage(20, 40, reply, name=name)

		return 0
