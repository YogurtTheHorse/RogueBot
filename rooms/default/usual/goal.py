from localizations import locale_manager
from constants import DICE_MAX

name = locale_manager.get('rooms.default.usual.goal.phrase_1')

actions = [ locale_manager.get('rooms.default.usual.goal.phrase_2'), locale_manager.get('rooms.default.usual.goal.phrase_3')]


def get_actions(user):
	return actions


def dice(user, reply, result, subject=None):
	if result <= DICE_MAX:
		msg = (
			'Держи золото: {0} монет.'
		)

		gold = 10 + result

		reply(msg.format(gold))
		user.give_gold(gold)

	else:
		msg = (
			locale_manager.get('rooms.default.usual.goal.phrase_4'))

		reply(msg, photo='BQADAgAD3wgAAmrZzgdOxgndC2991gI')
		user.make_damage(10, 30, reply, name=locale_manager.get('rooms.default.usual.goal.phrase_5'))

	user.leave(reply)


def action(user, reply, text):
	if text == actions[0]:
		user.throw_dice(reply)

	else:
		msg = (
			locale_manager.get('rooms.default.usual.goal.phrase_6'))

		reply(msg, photo='BQADAgAD3wgAAmrZzgdOxgndC2991gI')
		user.make_damage(10, 30, reply, name=locale_manager.get('rooms.default.usual.goal.phrase_7'))
		user.leave(reply)
