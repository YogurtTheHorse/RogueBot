from localizations import locale_manager
name = locale_manager.get('rooms.default.usual.apple_tree.phrase_1')

actions = [ locale_manager.get('rooms.default.usual.apple_tree.phrase_2'), locale_manager.get('rooms.default.usual.apple_tree.phrase_3')]

def get_actions(user):
	return actions

def enter(user, reply):
	msg = (
		locale_manager.get('rooms.default.usual.apple_tree.phrase_4'))
	reply(msg)

def action(user, reply, text):
	if text == actions[0]:
		reply(locale_manager.get('rooms.default.usual.apple_tree.phrase_5'))

		reply(locale_manager.get('rooms.default.usual.apple_tree.phrase_6'))

		user.hp = min(user.max_hp, user.hp + 50)
		user.add_item('loot', 'apple')
	else:
		reply(locale_manager.get('rooms.default.usual.apple_tree.phrase_7'))
		user.make_damage(20, 30, reply, name=name)

	user.leave(reply)
