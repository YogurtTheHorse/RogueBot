name = 'Сокровищница'

UP = 'NEVER GONNA GIVE YOU UP!'
DOWN = 'NEVER GONNA LET YOU DOWN!'
AROUND = 'NEVER GONNA RUN AROUND!'
DESERT = 'AND DESERT YOU!'

CRY = 'NEVER GONNA MAKE YOU CRY!'
GOODBYE = 'NEVER GONNA SAY GOODBYE'

NICE = 'Молодец. Но впредь не будь настолько алчным.'
WRONG = '*НЕПРАВИЛЬНО!*'

APPEAR = 'ПОЯВЛЯЕТСЯ РИК ЭСТЛИ И БЬЕТ ТЕБЯ МИКРОФОНОМ!'

def enter(user, reply):
	msg = (
		'Здесь горы из всевозможных сокровищ и тысячи, нет, миллионы золо...\n*О НЕТ, БЕГИ ЗА СВОЮ ЖИ...*\n'
	)
	reply(msg)
	user.set_room_temp('question', 'first')

def get_actions(user):
	question = user.get_room_temp('question', def_val='first')
	
	if question == 'first':
		return [ UP ]
	elif question == 'second':
		return [ AROUND ]
	elif question == 'third':
		return [ CRY, GOODBYE ]

def action(user, reply, text):
	question = user.get_room_temp('question', def_val='first')

	if question == 'first':
		reply(DOWN)
		user.set_room_temp('question', 'second')
	elif question == 'second':
		reply(DESERT)
		user.set_room_temp('question', 'third')
	elif question == 'third':
		if text == CRY:
			reply(NICE)
			user.leave(reply)
		else:
			reply(WRONG)
			reply(APPEAR)
			user.make_damage(50, 50, reply, name='Рик Астли')
			user.leave(reply)