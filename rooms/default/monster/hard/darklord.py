from localizations import locale_manager
from constants import *

FIGHT = locale_manager.get('rooms.default.monster_hard.darklord.phrase_7')
ESCAPE = locale_manager.get('rooms.default.monster_hard.darklord.phrase_8')

name = locale_manager.get('rooms.default.monster_hard.darklord.phrase_9')
hp = 1000  # Темный Лорд должен быть лютым парнем! А то что-то они там все перекаченные какие-то.
damage_range = ( 20, 25 )

coins = 0  # Темному Лорду не нужны деньги! Он берет все что захочет!

loot = [ 'ring' ]


def enter(user, reply):
	reply(
		locale_manager.get('rooms.default.monster_hard.darklord.phrase_1').format(name),
		photo='BQADAgAD_ggAAmrZzgfWmyCl_kraUgI'
	)

	if user.rooms_count < 500000:
		reply(
			locale_manager.get('rooms.default.monster_hard.darklord.phrase_2'))

		user.leave(reply)

	else:

		if not user.has_item('rigs'):
			reply(
				locale_manager.get('rooms.default.monster_hard.darklord.phrase_3'))

		else:
			user.remove_item('rigs')  # У игрока должно быть только одно кольцо!
			reply(
				locale_manager.get('rooms.default.monster_hard.darklord.phrase_4'))
		user.leave(reply)


def dice(user, reply, result, subject=None):

	if subject == ESCAPE:

		if result > DICE_MIDDLE:
			reply(locale_manager.get('rooms.default.monster_hard.darklord.phrase_10'))
			user.leave(reply)

		else:
			reply(locale_manager.get('rooms.default.monster_hard.darklord.phrase_11'))
			# тут нужно запустить обычый бой


def action(user, reply, text):
	question = user.get_room_temp('question')

	if text == FIGHT:
		reply(
			locale_manager.get('rooms.default.monster_hard.darklord.phrase_5'))
		# тут нужно запустить обычый бой


	elif text == ESCAPE:
		reply(
			locale_manager.get('rooms.default.monster_hard.darklord.phrase_6'))
		user.throw_dice(reply, ESCAPE)


def get_actions(user):
	return [FIGHT, ESCAPE]
