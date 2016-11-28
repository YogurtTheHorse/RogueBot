from localizations import locale_manager
name = locale_manager.get('items.neutral.necronomicone.phrase_1')
description = locale_manager.get('items.neutral.necronomicone.phrase_2')
price = 600

disposable = True
usable = True
def on_use(user, reply):
	if user.has_item('puzzle'):
		reply(locale_manager.get('items.neutral.necronomicone.phrase_3'))
	else:
		user.open_room(reply, 'special', 'the_thing_from_below')