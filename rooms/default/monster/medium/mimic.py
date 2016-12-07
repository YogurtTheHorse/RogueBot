from localizations import locale_manager
name = locale_manager.get('rooms.default.monster_medium.mimic.phrase_2')

ACTIVATED = 'activated'
actions = [locale_manager.get('rooms.default.monster_medium.mimic.phrase_3'), locale_manager.get('rooms.default.monster_medium.mimic.phrase_4')]

hp = 50
damage_range = (50, 50)

coins = 150

loot = []


def get_actions(user):
	if user.get_room_temp(ACTIVATED, True):
		return user.get_fight_actions()
	else:
		return actions


def enter(user, reply):
	reply(locale_manager.get('rooms.default.monster_medium.mimic.phrase_5'), photo='BQADAgADCQkAAmrZzgfwfl33PblsWQI')

	user.set_room_temp(ACTIVATED, False)


def action(user, reply, text):
	if user.get_room_temp(ACTIVATED, True):
		user.fight_action(reply, text)
	else:
		if text == actions[0]:
			if user.rooms_count < 25:
				reply(locale_manager.get('rooms.default.monster_medium.mimic.phrase_6'))
				user.leave(reply)
			else:
				reply(
					locale_manager.get('rooms.default.monster_medium.mimic.phrase_1'))
				user.set_room_temp(ACTIVATED, True)
		else:
			user.leave(reply)