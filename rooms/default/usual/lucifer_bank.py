from localizations import locale_manager
import databasemanager

name = locale_manager.get('rooms.default.usual.lucifer_bank.phrase_2')

def get_actions(user):
	return [ locale_manager.get('rooms.default.usual.lucifer_bank.phrase_3'), locale_manager.get('rooms.default.usual.lucifer_bank.phrase_4') ]

def enter(user, reply):
	reply(
		locale_manager.get('rooms.default.usual.lucifer_bank.phrase_1'),
		photo='BQADAgADSwkAAmrZzgc0tUQF067dNgI'
	)

def action(user, reply, text):
	if text == locale_manager.get('rooms.default.usual.lucifer_bank.phrase_5'):
		if user.gold < 5000:
			reply(locale_manager.get('rooms.default.usual.lucifer_bank.phrase_6'))
		else:
			user.gold = 0
			databasemanager.set_variable(str(user.uid) + '_gold', True)
			reply(locale_manager.get('rooms.default.usual.lucifer_bank.phrase_7'))
	else:
		reply(locale_manager.get('rooms.default.usual.lucifer_bank.phrase_8'))

	user.leave(reply)
