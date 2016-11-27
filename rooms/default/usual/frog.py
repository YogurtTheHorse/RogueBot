from localizations import locale_manager
name = locale_manager.get('rooms.default.usual.frog.phrase_1')

actions = [ locale_manager.get('rooms.default.usual.frog.phrase_2'), locale_manager.get('rooms.default.usual.frog.phrase_3')]

def get_actions(user):
	return actions

def enter(user, reply):
	msg = (
		locale_manager.get('rooms.default.usual.frog.phrase_4'))

	reply(msg, photo='BQADAgADPwkAAmrZzgd3oMWGzcJbhgI')

def action(user, reply, text):
	if text == actions[0]:
		msg = (
			locale_manager.get('rooms.default.usual.frog.phrase_5'))

		reply(msg)

		user.leave(reply)
	else:
		msg = (
			locale_manager.get('rooms.default.usual.frog.phrase_6'))

		reply(msg)

		user.add_item('good', 'fork')
		user.new_pet(reply, 'frog')
