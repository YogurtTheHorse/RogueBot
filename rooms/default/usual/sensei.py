from localizations import locale_manager
from constants import *

name = '先生'

room_type = 'other'

def get_actions(user):
	if user.has_tag(JAPANESE):
		return [ locale_manager.get('rooms.default.usual.sensei.phrase_1'), locale_manager.get('rooms.default.usual.sensei.phrase_2'), locale_manager.get('rooms.default.usual.sensei.phrase_3')]
	else:
		return [ '日本語を学びます', 'すでに日本語を知っていると言うこと', '静かに立ちます' ]

def enter(user, reply):
	if user.has_tag(JAPANESE):
		reply(locale_manager.get('rooms.default.usual.sensei.phrase_4'))
	else:
		reply('ようこそ！\n私はトトロです')

def action(user, reply, text):
	if text == get_actions(user)[0]:		
		if user.paid(50):
			reply('おめでとうございます!')

			user.add_tag(JAPANESE)
		else:
			reply(locale_manager.get('rooms.default.usual.sensei.phrase_5'))
			user.make_damage(20, 30, reply, death=False)
		
		user.leave(reply)
	elif text == get_actions(user)[1]:
		if user.has_tag(JAPANESE):
			reply(locale_manager.get('rooms.default.usual.sensei.phrase_6'))
			user.leave(reply)
		else:
			reply('私はトトロです')
	else:
		if user.has_tag(JAPANESE):
			reply(locale_manager.get('rooms.default.usual.sensei.phrase_7'))
		else:
			reply('私はトトロです')
