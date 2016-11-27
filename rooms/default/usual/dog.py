from localizations import locale_manager
name = locale_manager.get('rooms.default.usual.dog.phrase_1')

def get_actions(user):
	return [ ]

def enter(user, reply):
	reply(locale_manager.get('rooms.default.usual.dog.phrase_2'), photo='BQADAgADQQkAAmrZzgdOrJfjN97idgI')
	user.new_pet(reply, 'dog')

def action(user, reply, text):
	user.leave(reply)