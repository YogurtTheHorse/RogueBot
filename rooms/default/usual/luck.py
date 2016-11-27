from localizations import locale_manager
name = locale_manager.get('rooms.default.usual.luck.phrase_1')

def enter(user, reply):
	reply(locale_manager.get('rooms.default.usual.luck.phrase_2'))
	reply(locale_manager.get('rooms.default.usual.luck.phrase_3'), photo='BQADAgAD1wgAAmrZzgdfyW7V73sUzQI')
	user.make_damage(0, 25, reply, name=locale_manager.get('rooms.default.usual.luck.phrase_4'))
	user.leave(reply)

def get_actions(user):
	return [ ]


def action(user, reply, text):
	user.leave(reply)