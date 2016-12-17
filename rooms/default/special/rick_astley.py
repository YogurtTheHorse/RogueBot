from localizations import locale_manager
name = locale_manager.get('rooms.default.special.rick_astley.phrase_1')

UP = 'NEVER GONNA GIVE YOU UP!'
DOWN = 'NEVER GONNA LET YOU DOWN!'
AROUND = 'NEVER GONNA RUN AROUND!'
DESERT = 'AND DESERT YOU!'

CRY = 'NEVER GONNA MAKE YOU CRY!'
GOODBYE = 'NEVER GONNA SAY GOODBYE'

NICE = locale_manager.get('rooms.default.special.rick_astley.phrase_2')
WRONG = locale_manager.get('rooms.default.special.rick_astley.phrase_6')

APPEAR = locale_manager.get('rooms.default.special.rick_astley.phrase_3')

def enter(user, reply):
	msg = (
		locale_manager.get('rooms.default.special.rick_astley.phrase_4'))
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
			reply(NICE, photo='BQADAgADyggAAmrZzgc6EaeE79gQAAEC')
			user.leave(reply)
		else:
			reply(WRONG)
			reply(APPEAR)
			user.make_damage(50, 50, reply, name=locale_manager.get('rooms.default.special.rick_astley.phrase_5'))
			user.leave(reply)