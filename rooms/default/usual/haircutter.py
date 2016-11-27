from localizations import locale_manager
from constants import *

name = locale_manager.get('rooms.default.usual.haircutter.phrase_1')

room_type = 'other'
actions = [ locale_manager.get('rooms.default.usual.haircutter.phrase_2'), locale_manager.get('rooms.default.usual.haircutter.phrase_3'), locale_manager.get('rooms.default.usual.haircutter.phrase_4')]

def get_actions(user):
	return actions

def dice(user, reply, result, subject=None):
	if result > DICE_MIDDLE:
		reply(locale_manager.get('rooms.default.usual.haircutter.phrase_5'))
	else:
		reply(locale_manager.get('rooms.default.usual.haircutter.phrase_6'))

		if user.has_item('scissors'):
			user.remove_items_with_tag('scissors')
			reply(locale_manager.get('rooms.default.usual.haircutter.phrase_7'))

		user.make_damage(20, 30, reply, name=name)
	user.leave(reply)

def enter(user, reply):
	msg = (
		locale_manager.get('rooms.default.usual.haircutter.phrase_8'))
	reply(msg)

def action(user, reply, text):
	if text == actions[0]:
		user.remove_items_with_tag('hair')
		user.charisma += 10
		
		if user.paid(10):
			reply(locale_manager.get('rooms.default.usual.haircutter.phrase_9'))
		else:
			reply(locale_manager.get('rooms.default.usual.haircutter.phrase_10'))
			user.make_damage(20, 30, reply, name=name)
		
		user.leave(reply)
	elif text == actions[1]:
		reply(locale_manager.get('rooms.default.usual.haircutter.phrase_11'))
		user.throw_dice(reply)
	else:
		user.leave(reply)
