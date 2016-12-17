from localizations import locale_manager
import random
from constants import *

EVIL_COMISSAR = 'EVIL_COMISSAR'

READY = locale_manager.get('rooms.default.usual.comissar.phrase_2')
ESCAPE = locale_manager.get('rooms.default.usual.comissar.phrase_3')
FIGHT = locale_manager.get('rooms.default.usual.comissar.phrase_4')

name = locale_manager.get('rooms.default.usual.comissar.phrase_5')

def enter(user, reply):
	msg = (
		locale_manager.get('rooms.default.usual.comissar.phrase_1'))
	reply(msg, photo='BQADAgADHwEAAgy18wMAAWs-pH_tD3MC')
	user.set_room_temp('question', 'first')

def dice(user, reply, result, subject=None):
	if subject == ESCAPE:
		if result > (DICE_MAX / 3) * 2:
			reply(locale_manager.get('rooms.default.usual.comissar.phrase_6'))
			user.make_damage(10, 20, reply, name=name)
			user.leave(reply)
		elif result > DICE_MAX / 3:
			reply(locale_manager.get('rooms.default.usual.comissar.phrase_7'))
			user.make_damage(10, 20, reply)
			user.leave(reply)
		else:
			reply(locale_manager.get('rooms.default.usual.comissar.phrase_8'))
			user.death(reply, reason=name)
	elif subject == FIGHT:
		if result > DICE_MIDDLE:
			reply(locale_manager.get('rooms.default.usual.comissar.phrase_9'))
			user.add_tag(EVIL_COMISSAR)
			user.add_item('loot', 'laser_gun')
			user.leave(reply)
		else:
			reply(locale_manager.get('rooms.default.usual.comissar.phrase_10'))
			user.death(reply, reason=name)

def action(user, reply, text):
	question = user.get_room_temp('question', def_val='first')

	if question == 'first':
		if text == READY:
			reply(locale_manager.get('rooms.default.usual.comissar.phrase_11'))
			user.set_room_temp('question', 'smell')
		elif text == ESCAPE:
			reply(locale_manager.get('rooms.default.usual.comissar.phrase_12'))
			user.throw_dice(reply, ESCAPE)
		elif text == FIGHT:
			reply(locale_manager.get('rooms.default.usual.comissar.phrase_13'))
			user.throw_dice(reply, FIGHT)
	elif question == 'smell':
		if text == locale_manager.get('rooms.default.usual.comissar.phrase_14'):
			reply(locale_manager.get('rooms.default.usual.comissar.phrase_15'))
			user.set_room_temp('question', 'mage')
		else:
			reply(locale_manager.get('rooms.default.usual.comissar.phrase_16'))
			reply(locale_manager.get('rooms.default.usual.comissar.phrase_17'))

			user.throw_dice(reply, ESCAPE)
	elif question == 'mage':
		if text == locale_manager.get('rooms.default.usual.comissar.phrase_18'):
			reply(locale_manager.get('rooms.default.usual.comissar.phrase_19'))
			reply(locale_manager.get('rooms.default.usual.comissar.phrase_20'))

			user.throw_dice(reply, ESCAPE)
		else:
			reply(locale_manager.get('rooms.default.usual.comissar.phrase_21'))
			reply(locale_manager.get('rooms.default.usual.comissar.phrase_22'))

			reply(locale_manager.get('rooms.default.usual.comissar.phrase_23'))

			user.set_room_temp('question', 'poster')
	elif question == 'poster':
		if text == locale_manager.get('rooms.default.usual.comissar.phrase_24'):
			reply(locale_manager.get('rooms.default.usual.comissar.phrase_31'))
			reply(locale_manager.get('rooms.default.usual.comissar.phrase_25'))

			for i in range(7):
				user.add_item('neutral', 'laser_bullet')
			user.leave(reply)
		else:
			reply(locale_manager.get('rooms.default.usual.comissar.phrase_32'))
			reply(locale_manager.get('rooms.default.usual.comissar.phrase_26'))

			user.throw_dice(reply, ESCAPE)

def get_actions(user):
	question = user.get_room_temp('question', def_val='first')
	ans = [ ]

	if question == 'first':
		ans = [ READY, ESCAPE, FIGHT ]
	elif question == 'smell' or question == 'mage':
		ans = [ locale_manager.get('rooms.default.usual.comissar.phrase_27'), locale_manager.get('rooms.default.usual.comissar.phrase_28') ]
	else:
		ans = [ locale_manager.get('rooms.default.usual.comissar.phrase_29'), locale_manager.get('rooms.default.usual.comissar.phrase_30') ]

	random.shuffle(ans)

	return ans