from localizations import locale_manager
name = locale_manager.get('items.good.checkpoint.phrase_1')
description = locale_manager.get('items.good.checkpoint.phrase_2')
price = 10000

usable = True

def on_use(user, reply):
	if user.get_variable('was_checkpoint', def_val=False) is False:
		user.remove_item('checkpoint')
		user.set_variable('was_checkpoint', True)
		user.save()
		reply(locale_manager.get('items.good.checkpoint.phrase_3'))
	else:
		reply(locale_manager.get('items.good.checkpoint.phrase_4'))