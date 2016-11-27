from localizations import locale_manager
import usermanager

name = locale_manager.get('rooms.default.usual.orc_shop.phrase_2')

def enter(user, reply):
	usr = usermanager.random_user()
	msg = (
		locale_manager.get('rooms.default.usual.orc_shop.phrase_1'))
	reply(msg.format(usr.name))

def get_actions(user):
	return [ locale_manager.get('rooms.default.usual.orc_shop.phrase_3'), locale_manager.get('rooms.default.usual.orc_shop.phrase_4'), locale_manager.get('rooms.default.usual.orc_shop.phrase_5'), locale_manager.get('rooms.default.usual.orc_shop.phrase_6') ]

def action(user, reply, text):
	if text == locale_manager.get('rooms.default.usual.orc_shop.phrase_7'):
		teeth_cnt = user.get_room_temp('teeth_cnt', def_val=0)


		if user.has_item('tooth'):
			if teeth_cnt > 2:
				reply(locale_manager.get('rooms.default.usual.orc_shop.phrase_8'))
			else:
				user.set_room_temp('teeth_cnt', teeth_cnt + 1)

			reply(locale_manager.get('rooms.default.usual.orc_shop.phrase_9'))
		else:
			reply(locale_manager.get('rooms.default.usual.orc_shop.phrase_10'))
			user.make_damage(1, 10, reply, death=False)
	elif text == locale_manager.get('rooms.default.usual.orc_shop.phrase_11'):
		if user.items.count(('loot', 'tooth', {})) >= 5:
			reply(locale_manager.get('rooms.default.usual.orc_shop.phrase_12'))
			user.add_item('good', 'mage_stick')

			for i in range(5):
				user.remove_item('tooth')
		else:
			reply(locale_manager.get('rooms.default.usual.orc_shop.phrase_13'))
			user.make_damage(1, 10, reply, death=False)
	elif text == locale_manager.get('rooms.default.usual.orc_shop.phrase_14'):
		if user.items.count(('loot', 'tooth', {})) >= 5:
			reply(locale_manager.get('rooms.default.usual.orc_shop.phrase_15'))
			user.add_item('neutral', 'protein')

			for i in range(5):
				user.remove_item('tooth')
		else:
			reply(locale_manager.get('rooms.default.usual.orc_shop.phrase_16'))
			user.make_damage(1, 10, reply, death=False)
	else:
		user.leave(reply)