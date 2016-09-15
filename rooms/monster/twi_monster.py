import twimanager

name = 'Твиттер-блоггер'
hp = 1
damage_range =  ( 15, 20 )

coins = 0

loot = [ ]

def on_death(user, reply):
	twimanager.dead(user)

def on_won(user, reply):
	twimanager.won(user)

def on_leave(user, reply):
	twimanager.leave(user)

def enter(user, reply):
	can_enter, status = twimanager.status()

	if can_enter:
		twimanager.enter(user)
		reply(
			'«Привет! У меня есть микроблог! Настоящий! Вот тут: twitter.com/funrogbot.\n'
			'Я уже запостил про тебя инфу! Классно, да? Круто же!»\n\n'
			'_Тебе захотелось побить его._'
		)
	else:
		if status == 'busy':
			reply(
				'Его охрана выставила тебя за дверь, у него сейчас посетитель.\n'
				'За подробности обращаться сюда: twitter.com/funrogbot\n\n'
				'«Охрана у школьника?..»'
			)
		else:
			reply('Он спит — приходи попозже.')
			#reply(
			#	'Он спит — приходи попозже, что именно ему сниться можно посмотреть вот тут — twitter.com/funrogbot.'
			#)
			
		user.leave(reply)