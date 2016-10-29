name = 'Сундук'

ACTIVATED = 'activated'
actions = ['Открыть сундук', 'Уйти']

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
	reply('Ты заходишь в комнату и видишь сундук.\nОбычный сундук.', photo='BQADAgADCQkAAmrZzgfwfl33PblsWQI')

	user.set_room_temp(ACTIVATED, False)


def action(user, reply, text):
	if user.get_room_temp(ACTIVATED, True):
		user.fight_action(reply, text)
	else:
		if text == actions[0]:
			if user.rooms_count < 25:
				reply('Не открывается')
				user.leave(reply)
			else:
				reply(
					'Ты подходишь к сундуку...\n'
					'...\n'
					'...\n'
					'...\n'
					'...\n'
					'...\n'
					'_МИМИК_\n'
				)
				user.set_room_temp(ACTIVATED, True)
		else:
			user.leave(reply)