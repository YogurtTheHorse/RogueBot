from localizations import locale_manager
from localizations import locale_manager
from constants import *
import random

name = locale_manager.get('rooms.default.usual.troll_bridge.phrase_1')

c_PRICE             = 75        # Стоимость прохода 
c_MIN_ROOM_COUNT    = 200       # Мин комнат
c_MIN_STRENGTH_ANSW = 100       # Мин силы для нападения
c_MIN_INTELL_ANSW   = 100       # Мин интелекта для ответа
c_TROLL_R1          = locale_manager.get('rooms.default.usual.troll_bridge.phrase_101').format(c_PRICE)
c_TROLL_R2          = locale_manager.get('rooms.default.usual.troll_bridge.phrase_102')

GO     = locale_manager.get('rooms.default.usual.troll_bridge.phrase_2')
LEAVE  = locale_manager.get('rooms.default.usual.troll_bridge.phrase_3')
ESCAPE = locale_manager.get('rooms.default.usual.troll_bridge.phrase_4')
GUP    = locale_manager.get('rooms.default.usual.troll_bridge.phrase_5')
PAY    = locale_manager.get('rooms.default.usual.troll_bridge.phrase_6')
EAT    = locale_manager.get('rooms.default.usual.troll_bridge.phrase_7')
FIGHT  = locale_manager.get('rooms.default.usual.troll_bridge.phrase_8')
CHEAT  = locale_manager.get('rooms.default.usual.troll_bridge.phrase_9')

def enter(user, reply):
	msg = (
		locale_manager.get('rooms.default.usual.troll_bridge.phrase_10')
	)
	reply(msg, photo='BQADAgAD2wgAAmrZzgdIlwyFp4vXPwI')
	user.set_room_temp('question', 'first')

def dice(user, reply, result, subject=None):
	if subject == ESCAPE:
		if  result > (DICE_MAX / 4) * 3:
			reply(locale_manager.get('rooms.default.usual.troll_bridge.phrase_11'))
			user.make_damage(10,15,reply)
			user.leave(reply)
		elif result < DICE_MAX / 4:
			reply(locale_manager.get('rooms.default.usual.troll_bridge.phrase_12'))
			user.death(reply, reason=name)
		else:
			reply(locale_manager.get('rooms.default.usual.troll_bridge.phrase_13'))
			if user.has_item('sunion_helmet'):
				reply(c_TROLL_R2)
				user.leave(reply)
			else:
				reply(c_TROLL_R1)
				user.set_room_temp('question','underbridge')
	elif subject == FIGHT:
		if  result > (DICE_MAX / 5) * 4:
			reply(locale_manager.get('rooms.default.usual.troll_bridge.phrase_14'))
			reply(locale_manager.get('rooms.default.usual.troll_bridge.phrase_15'))
			user.add_item('loot','sunion_helmet')
			user.give_gold(random.randrange(5,100,5))
			user.leave(reply)
		else:
			reply(locale_manager.get('rooms.default.usual.troll_bridge.phrase_16'))
			user.death(reply, reason=name)


def action(user, reply, text):
	question = user.get_room_temp('question',def_val='first')

	if question == 'first':
		if text == GO:
			if user.rooms_count < c_MIN_ROOM_COUNT:                      
				reply(locale_manager.get('rooms.default.usual.troll_bridge.phrase_17'))
				user.add_item('neutral','coin')
				user.leave(reply)
			else:
				reply(locale_manager.get('rooms.default.usual.troll_bridge.phrase_18'))
				user.set_room_temp('question','scarryhand')
		elif text == LEAVE:
			reply(locale_manager.get('rooms.default.usual.troll_bridge.phrase_19'))
			user.leave(reply)
	elif question == 'scarryhand':
			if text == GUP: 
				reply(locale_manager.get('rooms.default.usual.troll_bridge.phrase_20'))
				if user.has_item('sunion_helmet'):
					reply(c_TROLL_R2)
					user.leave(reply)
				else:
					reply(c_TROLL_R1)
					user.set_room_temp('question','underbridge')
			elif text == ESCAPE:
				user.throw_dice(reply, ESCAPE)
	elif question == 'underbridge':
			if text == FIGHT:
				user.throw_dice(reply, FIGHT)
			elif text == PAY:
				if user.paid(c_PRICE):
					reply(locale_manager.get('rooms.default.usual.troll_bridge.phrase_21'))
				else:
					reply(locale_manager.get('rooms.default.usual.troll_bridge.phrase_22'))
					user.make_damage(40,70,reply,name=name)
				user.leave(reply)
			elif text == EAT:
				reply(locale_manager.get('rooms.default.usual.troll_bridge.phrase_23'))
				user.death(reply, reason=name)
			elif text == CHEAT:
				reply(locale_manager.get('rooms.default.usual.troll_bridge.phrase_103'))
				user.add_item('loot','sunion_helmet')
				user.leave(reply)

def get_actions(user):
	question  = user.get_room_temp('question',def_val='first')
	answers = []

	if question == 'first':
		answers = [ GO, LEAVE ]
	if question == 'scarryhand':
		answers = [ GUP, ESCAPE ]
	if question == 'underbridge':
		answers = [ PAY, EAT ]
		if user.damage >= c_MIN_STRENGTH_ANSW:
			answers += [ FIGHT ]
		if user.mana_damage >= c_MIN_INTELL_ANSW:
			answers += [ CHEAT ]
	random.shuffle(answers)
	return answers
