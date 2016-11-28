from localizations import locale_manager
name = locale_manager.get('items.neutral.sign.phrase_1')
description = locale_manager.get('items.neutral.sign.phrase_2')

price = 300

usable = True

def on_use(user, reply):
	user.open_room(reply, 'special', 'sign')
