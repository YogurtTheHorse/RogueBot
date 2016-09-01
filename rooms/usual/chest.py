import random

name = 'Сундук'

actions = ['Открыть сундку', 'Уйти']


def get_actions(user):
	return actions


def enter(user, reply):
	reply('Ты заходишь в комнату и видешь сундук.\nОбычный сундук')


def action(user, reply, text):

	if text == actions[0]:
		reply(
			'Ты подходишь к сундуку...\n'
			'...\n'
			'...\n'
			'...\n'
			'...\n'
			'...\n'
			'Поднимаешь крышку\n'
		)

		if random.random > 0.5:
			reply('Пусто\nОчень жаль. Повезет в следующий раз.')

		else:

			generator = random.randrange(0, 5, 1)

			if generator == 1:
				reply('В сундуке был Банан')
				user.add_item('loot', 'banana')
			elif generator == 2:
				reply('В сундуке был Крыло крысы-летяги')
				user.add_item('loot', 'bat_wing')
			elif generator == 3:
				reply('В сундуке был Указатель')
				user.add_item('neutral', 'sing')
			elif generator == 4:
				reply('В сундуке был Трезубец')
				user.add_item('special', 'trident', )
			else:
				reply('В сундуке был Амулет мага')
				user.add_item('loot', 'mage_amulet')

	user.leave(reply)