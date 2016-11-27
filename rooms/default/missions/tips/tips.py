from localizations import locale_manager
import random

name = locale_manager.get('rooms.default.missions_tips.tips.phrase_1')

tips = [
	locale_manager.get('rooms.default.missions_tips.tips.phrase_2'),
	locale_manager.get('rooms.default.missions_tips.tips.phrase_3'),
	locale_manager.get('rooms.default.missions_tips.tips.phrase_4'),
	locale_manager.get('rooms.default.missions_tips.tips.phrase_5'),
	locale_manager.get('rooms.default.missions_tips.tips.phrase_6'),
	locale_manager.get('rooms.default.missions_tips.tips.phrase_7'),
	locale_manager.get('rooms.default.missions_tips.tips.phrase_8')
]

actions = [ locale_manager.get('rooms.default.missions_tips.tips.phrase_9'), locale_manager.get('rooms.default.missions_tips.tips.phrase_10') ]

def get_actions(user):
	return actions

def enter(user, reply):
	reply(locale_manager.get('rooms.default.missions_tips.tips.phrase_11'))

def action(user, reply, text):
	if text == actions[0]:
		reply(random.choice(tips), photo='BQADAgADUQkAAmrZzgeh8l758pmZEQI')

		user.new_mission('tips', 'tips', path_len=25)
	else:
		reply(locale_manager.get('rooms.default.missions_tips.tips.phrase_12'))
	user.leave(reply)