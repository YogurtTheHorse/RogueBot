from localizations import locale_manager
import random

name = locale_manager.get('rooms.vietnam.missions_tips.tips.phrase_1')

tips = [
	locale_manager.get('rooms.vietnam.missions_tips.tips.phrase_2'),
	locale_manager.get('rooms.vietnam.missions_tips.tips.phrase_3'),
	locale_manager.get('rooms.vietnam.missions_tips.tips.phrase_4'),
	locale_manager.get('rooms.vietnam.missions_tips.tips.phrase_5'),
	locale_manager.get('rooms.vietnam.missions_tips.tips.phrase_6'),
	locale_manager.get('rooms.vietnam.missions_tips.tips.phrase_7')
]

actions = [ locale_manager.get('rooms.vietnam.missions_tips.tips.phrase_8'), locale_manager.get('rooms.vietnam.missions_tips.tips.phrase_9') ]

def get_actions(user):
	return actions

def enter(user, reply):
	reply(locale_manager.get('rooms.vietnam.missions_tips.tips.phrase_10'))

def action(user, reply, text):
	if text == actions[0]:
		reply(random.choice(tips))

		user.new_mission('tips', 'tips', path_len=25)
	else:
		reply(locale_manager.get('rooms.vietnam.missions_tips.tips.phrase_11'))
	user.leave(reply)