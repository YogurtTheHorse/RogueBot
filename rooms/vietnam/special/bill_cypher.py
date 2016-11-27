from localizations import locale_manager
ESCAPE = locale_manager.get('rooms.default.special.bill_cypher.phrase_2')
READY = locale_manager.get('rooms.default.special.bill_cypher.phrase_3')
FIGHT = locale_manager.get('rooms.default.special.bill_cypher.phrase_4')

name = locale_manager.get('rooms.default.special.bill_cypher.phrase_5')

def enter(user, reply):
	msg = (
		locale_manager.get('rooms.default.special.bill_cypher.phrase_1'))
	reply(msg)

	user.set_room_temp('question', 'first')

def get_actions(user):
	question = user.get_room_temp('question', def_val='first')
	
	if question == 'first':
		return [ ESCAPE, READY, FIGHT ]
	else:
		return [ locale_manager.get('rooms.default.special.bill_cypher.phrase_6'), locale_manager.get('rooms.default.special.bill_cypher.phrase_7') ]

def action(user, reply, text):
	question = user.get_room_temp('question', def_val='first')

	if question == 'first':
		if text == ESCAPE:
			reply(locale_manager.get('rooms.default.special.bill_cypher.phrase_8'))
			user.max_hp += 20
			user.leave(reply)
		elif text == READY:
			reply(locale_manager.get('rooms.default.special.bill_cypher.phrase_9'))
			user.set_room_temp('question', 'negotiate')
		elif text == FIGHT:
			reply(locale_manager.get('rooms.default.special.bill_cypher.phrase_10'))
			user.reborn(reply, locale_manager.get('rooms.default.special.bill_cypher.phrase_11'), name=locale_manager.get('rooms.default.special.bill_cypher.phrase_12'))
	elif question == 'negotiate':
		if text == locale_manager.get('rooms.default.special.bill_cypher.phrase_13'):
			reply(locale_manager.get('rooms.default.special.bill_cypher.phrase_14'))
			user.gold += 4000
			user.leave(reply)
		else:
			reply(locale_manager.get('rooms.default.special.bill_cypher.phrase_15'))
			user.reborn(reply, locale_manager.get('rooms.default.special.bill_cypher.phrase_16'), name=locale_manager.get('rooms.default.special.bill_cypher.phrase_17'))
