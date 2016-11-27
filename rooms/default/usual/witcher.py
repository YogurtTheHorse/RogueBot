from localizations import locale_manager
name = locale_manager.get('rooms.default.usual.witcher.phrase_1')

ASK = locale_manager.get('rooms.default.usual.witcher.phrase_2')
CAN_I_HELP = '— Может, тебе помочь?'
HELP = locale_manager.get('rooms.default.usual.witcher.phrase_3')
WAIT = locale_manager.get('rooms.default.usual.witcher.phrase_4')

def enter(user, reply):
	reply(
		locale_manager.get('rooms.default.usual.witcher.phrase_5'))
	user.set_room_temp('question', 'first')
	user.set_room_temp('cnt', 0)

def action(user, reply, text):
	question = user.get_room_temp('question', def_val='first')

	cnt = user.get_room_temp('cnt', 0) + 1
	user.set_room_temp('cnt', cnt)
	if text == ASK:
		reply(locale_manager.get('rooms.default.usual.witcher.phrase_6'))
		user.leave(reply)
	elif text == CAN_I_HELP:
		reply('— Не надо, я сам! Я ведьмак, или ты?!')
		user.set_room_temp('question', 'third')
	elif text == HELP:
		reply(
			locale_manager.get('rooms.default.usual.witcher.phrase_7'))
		user.leave(reply)
	else:
		reply('— Сейчас достану, подожди...')
		if cnt > 1:
			user.set_room_temp('question', 'second')

def get_actions(user):
	question = user.get_room_temp('question', def_val='first')

	if question == 'first':
		return [ WAIT, ASK ]
	elif question == 'second':
		return [ CAN_I_HELP, ASK ]
	else:
		return [ HELP, ASK ]