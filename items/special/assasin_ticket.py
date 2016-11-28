from localizations import locale_manager
name = locale_manager.get('items.special.assasin_ticket.phrase_1')
description = locale_manager.get('items.special.assasin_ticket.phrase_2')
price = 0

disposable = True
fightable = True

def fight_use(user, reply, room):
	reply(locale_manager.get('items.special.assasin_ticket.phrase_3'))

	return 9000