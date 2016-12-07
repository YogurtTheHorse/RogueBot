from localizations import locale_manager
from constants import OLDMAN_STICKER

name = locale_manager.get('rooms.default.missions_main.first.phrase_1')

actions = [ locale_manager.get('rooms.default.missions_main.first.phrase_2'), locale_manager.get('rooms.default.missions_main.first.phrase_3')]

def get_actions(user):
	return actions

def enter(user, reply):
	reply(locale_manager.get('rooms.default.missions_main.first.enter_phrase'), photo=OLDMAN_STICKER)

	user.add_item('story', 'gun')
	user.add_item('story', 'map')
	user.add_item('neutral', 'bullet')
	user.add_item('story', 'glasses')


	user.new_mission('main', 'second', 10)

def action(user, reply, text):
	if text == actions[0]:
		reply('...')
	else:
		user.leave(reply)