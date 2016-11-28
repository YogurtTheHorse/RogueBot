from localizations import locale_manager

name = locale_manager.get('items.bad.voodoo.phrase_1')

description = locale_manager.get('items.bad.voodoo.phrase_2')

price = 50

def on_room(user, reply, room):	
	reply(locale_manager.get('items.bad.voodoo.phrase_3'))
	user.make_damage(20,30, reply, death=False)
