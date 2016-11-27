from localizations import locale_manager
from constants import *

READY = locale_manager.get('rooms.default.usual.slender.phrase_1')
ESCAPE = locale_manager.get('rooms.default.usual.slender.phrase_2')

name = locale_manager.get('rooms.default.usual.slender.phrase_3')

def enter(user, reply):
	reply(locale_manager.get('rooms.default.usual.slender.phrase_4'), photo=FOG_STICKER)
	user.set_room_temp('question', 'first')

def action(user,reply, text):
	question = user.get_room_temp('question', def_val='first')

	if question == 'first':
		if text == READY:
			reply(locale_manager.get('rooms.default.usual.slender.phrase_5'))
			user.set_room_temp('question', 'second')
		else:
			reply(locale_manager.get('rooms.default.usual.slender.phrase_6'))
			user.leave(reply)
	elif question == 'second':
		if text == locale_manager.get('rooms.default.usual.slender.phrase_7'):
			reply('Ты снимаешь листок с дерева и осматриваешь. На обратной стороне ты замечаешь надпись крупными буквами:\nВСЕГДА СМОТРИТ. НЕТ ГЛАЗ.\n1/4\nГде-то вдалеке ты слышишь шум.')
			user.set_room_temp('question', 'third')
	elif question == 'third':
		if text == locale_manager.get('rooms.default.usual.slender.phrase_8'):
			reply('Шум усиливается, внезапно из-за деревьев возник неестественно высокий человек.\nТы не можешь двигаться.\nТьма окутала твоё сознание.', photo='BQADAgAD4AgAAmrZzgdmsBNDB5hPiQI')
			user.death(reply, reason=locale_manager.get('rooms.default.usual.slender.phrase_9'))
		else:
			reply(locale_manager.get('rooms.default.usual.slender.phrase_10'))
			user.set_room_temp('question', 'forth')
	elif question == 'forth':
		if text == locale_manager.get('rooms.default.usual.slender.phrase_11'):
			reply('Ты подошел к вышке. Осмотрев ее, ты обнаруживаешь на одной из опор еще один лист бумаги.\nНа обратной стороне рисунок человека с неестественно длинными конечностями и текст:\nНЕТ НЕТ НЕТ НЕТ НЕТ НЕТ НЕТ НЕТ.\n2/4\nТы снова слишишь шум, но в этот раз ближе и громче.')
			user.set_room_temp('question', 'fifth')
	elif question =='fifth':
		if text == locale_manager.get('rooms.default.usual.slender.phrase_12'):
			reply(locale_manager.get('rooms.default.usual.slender.phrase_13'))
			user.set_room_temp('question', 'seventh')
		else:
			reply(locale_manager.get('rooms.default.usual.slender.phrase_14'), photo='BQADAgAD4AgAAmrZzgdmsBNDB5hPiQI')
			user.set_room_temp('question', 'sixth')
	elif question == 'sixth':
		if text == locale_manager.get('rooms.default.usual.slender.phrase_15'):
			reply(locale_manager.get('rooms.default.usual.slender.phrase_16'))
			user.set_room_temp('question', 'seventh')
	elif question == 'seventh':
		if text == locale_manager.get('rooms.default.usual.slender.phrase_17'):
			reply(locale_manager.get('rooms.default.usual.slender.phrase_18'))
			user.set_room_temp('question', 'eighth')
	elif question == 'eighth':
		if text == locale_manager.get('rooms.default.usual.slender.phrase_19'):
			reply('Взяв в руки лист бумаги ты обнаруживаешь на другой стороне надпись :\nНЕ СМОТРИ....\nИЛИ ОН ЗАБЕРЕТ ТЕБЯ.\n3/4\nПрочитав этот текст ты вновь услышал шум.')
			user.set_room_temp('question', 'nineth')
	elif question == 'nineth':
		if text == locale_manager.get('rooms.default.usual.slender.phrase_20'):
			reply('Выбежав из ангара, ты столкнулся с ним лицом к лицу.\nТьма окутала твоё сознание', photo='BQADAgAD4AgAAmrZzgdmsBNDB5hPiQI')
			user.death(reply, reason=locale_manager.get('rooms.default.usual.slender.phrase_21'))
		else:
			reply(locale_manager.get('rooms.default.usual.slender.phrase_22'))
			user.set_room_temp('question', 'tenth')
	elif question == 'tenth':
		if text == locale_manager.get('rooms.default.usual.slender.phrase_23'):
			reply(locale_manager.get('rooms.default.usual.slender.phrase_24'))
			user.set_room_temp('question', 'eleventh')
	elif question == 'eleventh':
		if text == locale_manager.get('rooms.default.usual.slender.phrase_25'):
			reply(locale_manager.get('rooms.default.usual.slender.phrase_26'))
			user.set_room_temp('question', 'dozenth')
	elif question == 'dozenth':
		if text == locale_manager.get('rooms.default.usual.slender.phrase_27'):
			reply('Это было глупо.\nТьма окутала твоё сознание.')
			user.death(reply, reason=locale_manager.get('rooms.default.usual.slender.phrase_28'))
		else:
			reply(locale_manager.get('rooms.default.usual.slender.phrase_29'))
			user.set_room_temp('question', 'thirteenth')
	elif question == 'thirteenth':
		if text == locale_manager.get('rooms.default.usual.slender.phrase_30'):
			reply('Шум стал громче, твоё сердцебиение участилось. Заглянув за очередной трейлер, ты обнаруживаешь скомканную бумажку. Развернув ее ты видишь большую надпись:\nНЕЛЬЗЯ УБЕЖАТЬ\n4/4\nТебя затрясло, ведь ты не понимаешь, как же так, все это было зря? Но твои размышления прервал усилившийся шум.')
			user.set_room_temp('question', 'fourteenth')
	elif question == 'fourteenth':
		if text == locale_manager.get('rooms.default.usual.slender.phrase_31'):
			reply(locale_manager.get('rooms.default.usual.slender.phrase_32'))
			user.set_room_temp('question', 'fifteenth')
	elif question == 'fifteenth':
		if text == locale_manager.get('rooms.default.usual.slender.phrase_33'):
			reply(locale_manager.get('rooms.default.usual.slender.phrase_34'))
			user.set_room_temp('question', 'sixteenth')	
	elif question == 'sixteenth':
		if text == locale_manager.get('rooms.default.usual.slender.phrase_35'):
			reply('Ты же не думал, что получится?\nТьма окутала твоё сознание.')
			user.death(reply, reason=locale_manager.get('rooms.default.usual.slender.phrase_36'))
		else:
			reply(locale_manager.get('rooms.default.usual.slender.phrase_37'))
			user.set_room_temp('question', 'seventeenth')
	elif question == 'seventeenth':
		if text == locale_manager.get('rooms.default.usual.slender.phrase_38'):
			reply(locale_manager.get('rooms.default.usual.slender.phrase_39'))
			user.gold += 100
			user.leave(reply)

def get_actions(user):
	question = user.get_room_temp('question', def_val='first')
	ans = [ ]

	if question == 'first':
		ans = [ READY, ESCAPE ]
	elif question == 'second':
		ans = [ locale_manager.get('rooms.default.usual.slender.phrase_40') ]
	elif question == 'third':
		ans = [ locale_manager.get('rooms.default.usual.slender.phrase_41'), locale_manager.get('rooms.default.usual.slender.phrase_42') ]
	elif question == 'forth':
		ans = [ locale_manager.get('rooms.default.usual.slender.phrase_43') ]
	elif question == 'fifth':
		ans = [ locale_manager.get('rooms.default.usual.slender.phrase_44'), locale_manager.get('rooms.default.usual.slender.phrase_45') ]
	elif question == 'sixth':
		ans = [ locale_manager.get('rooms.default.usual.slender.phrase_46') ]
	elif question == 'seventh':
		ans = [ locale_manager.get('rooms.default.usual.slender.phrase_47') ]
	elif question == 'eighth':
		ans = [ locale_manager.get('rooms.default.usual.slender.phrase_48') ]
	elif question == 'nineth':
		ans = [ locale_manager.get('rooms.default.usual.slender.phrase_49'), locale_manager.get('rooms.default.usual.slender.phrase_50') ]
	elif question == 'tenth':
		ans = [ locale_manager.get('rooms.default.usual.slender.phrase_51') ]
	elif question == 'eleventh':
		ans = [ locale_manager.get('rooms.default.usual.slender.phrase_52') ]
	elif question == 'dozenth':
		ans = [ locale_manager.get('rooms.default.usual.slender.phrase_53'), locale_manager.get('rooms.default.usual.slender.phrase_54') ]
	elif question == 'thirteenth':
		ans = [ locale_manager.get('rooms.default.usual.slender.phrase_55') ]
	elif question == 'fourteenth':
		ans = [ locale_manager.get('rooms.default.usual.slender.phrase_56') ]
	elif question == 'fifteenth':
		ans = [ locale_manager.get('rooms.default.usual.slender.phrase_57') ]
	elif question == 'sixteenth':
		ans = [ locale_manager.get('rooms.default.usual.slender.phrase_58'), locale_manager.get('rooms.default.usual.slender.phrase_59') ]
	else:
		ans = [ locale_manager.get('rooms.default.usual.slender.phrase_60') ]

	return ans
