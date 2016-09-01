name = 'Сундук'

ACTVATED = 'activated'
actions = ['Открыть сундку', 'Уйти']

hp = 50
damage_range = (50, 50)

coins = 500

loot = []


def get_actions(user):
	if user.get_room_temp(ACTVATED, True):
		return user.get_fight_actions()

	else:
		return actions


def enter(user, reply):
	reply('Ты заходишь в комнату и видешь сундук.\nОбычный сундук')

	user.set_room_temp(ACTVATED, False)


def action(user, reply, text):
	if user.get_room_temp(ACTVATED, True):

		if text == actions[0]:
			reply(
				'Ты подходишь к сундуку...\n'
				'...\n'
				'...\n'
				'...\n'
				'...\n'
				'...\n'
				'_МИМИК_\n'
			)

			user.fight_action(reply)

	else:
		user.leave(reply)