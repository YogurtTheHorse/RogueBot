from localizations import locale_manager
from constants import *
from utils.buffs import DevilPower
from utils.buffs import DevilInt
from utils.buffs import DevilMoney
from utils.buffs import DevilEntity

name = locale_manager.get('rooms.default.usual.devil.phrase_1')

def enter(user, reply):
	reply(locale_manager.get('rooms.default.usual.devil.phrase_2'), photo='BQADAgADEgkAAmrZzgeGC93mbCR4mwI')
	user.set_room_temp('question', 'first')

def action(user, reply, text):
	question = user.get_room_temp('question', def_val='first')
	MADE_SOLUTION_TEXT = 'Отличный выбор, а теперь подпиши здесь и вот здесь.\nПеред вами возник исписанный на непонятном языке пергамент с двумя галочками.\n — Ну же, условия стандартные: когда умрешь я заберу твою душу.'
	CURSE_TEXT = ' изменился в лице, кажется ему не понравилось это. — Тогда вот тебе маленький подарок, чтобы ты знал, что не нужно отрывать меня от работы по пустякам.'

	if question == 'first':
		if text == locale_manager.get('rooms.default.usual.devil.phrase_3'):
			reply(locale_manager.get('rooms.default.usual.devil.phrase_4'))
		elif text == locale_manager.get('rooms.default.usual.devil.phrase_5'):
			reply(locale_manager.get('rooms.default.usual.devil.phrase_6'))
			user.set_room_temp('question', 'second')
		else:
			reply('На тебя не обратили внимания и ты ушёл.')
			user.leave(reply)
	elif question == 'second':
		if text == locale_manager.get('rooms.default.usual.devil.phrase_7'):
			reply(locale_manager.get('rooms.default.usual.devil.phrase_8'))
			user.leave(reply)
		elif text == locale_manager.get('rooms.default.usual.devil.phrase_9'):
			usr_name = user.name.lower()
			reply('У меня много имен, {0}. В разных культурах меня называли по-разному. Я помогал людям добиться превосходных результатов, начинал войны, насылал болезни.'.format(usr_name))
			user.set_room_temp('question', 'third')
	elif question == 'third':
		if text == locale_manager.get('rooms.default.usual.devil.phrase_10'):
			reply('Человек {0}'.format(CURSE_TEXT))
			user.max_hp -= 50
			user.leave(reply)
		elif text == locale_manager.get('rooms.default.usual.devil.phrase_11'):
			reply(locale_manager.get('rooms.default.usual.devil.phrase_12'))
			user.set_room_temp('question', 'forth')
		else:
			reply('Внезапно он исчез из виду и вы услышали шепот у себя в голове\n — Может ты хочешь бесконечную силу, чтобы все трепетали пред тобой?\nИли ты хочешь быть гением, способным на всё?\nХотя нет, наверное, ты хочешь несметного богатства?\nИли же всё сразу?\nВыбирай, смертный!')
			user.set_room_temp('question', 'fifth')
	elif question == 'forth':
		if text == locale_manager.get('rooms.default.usual.devil.phrase_13'):
			reply('Дьявол {0}'.format(CURSE_TEXT))
			user.max_hp -= 50
			user.leave(reply)
		elif text == locale_manager.get('rooms.default.usual.devil.phrase_14'):
			reply('Внезапно он исчез из виду и вы услышали шепот у себя в голове\n — Может ты хочешь бесконечную силу, чтобы все трепетали пред тобой?\nИли ты хочешь быть гением, способным на всё?\nХотя нет, наверное, ты хочешь несметного богатства?\nИли же всё сразу?\nВыбирай, смертный!')
			user.set_room_temp('question', 'fifth')
	elif question == 'fifth':
		if text == locale_manager.get('rooms.default.usual.devil.phrase_15'):
			reply(MADE_SOLUTION_TEXT)
			user.new_buff(DevilPower())
			user.add_tag(DEVIL)
			user.set_room_temp('question', 'sixth')
		elif text == locale_manager.get('rooms.default.usual.devil.phrase_16'):
			reply(MADE_SOLUTION_TEXT)
			user.new_buff(DevilInt())
			user.add_tag(DEVIL)
			user.set_room_temp('question', 'sixth')
		elif text == locale_manager.get('rooms.default.usual.devil.phrase_17'):
			reply(MADE_SOLUTION_TEXT)
			user.new_buff(DevilMoney())
			user.gold += 100000
			user.add_tag(DEVIL)
			user.set_room_temp('question', 'sixth')
		else:
			reply(' — Вот это жадность. Ты напоминаешь мне меня в молодости, я тогда тоже был ненасытен...\nДьявол улыбнулся своим воспоминаниям.\n — Вернемся к делу! Подпиши здесь и здесь.\nПеред вами возник исписанный на непонятном языке пергамент с двумя галочками.\n — Ну же, условия стандартные: когда умрешь я заберу твою душу.')
			user.new_buff(DevilEntity())
			user.gold += 100000
			user.add_tag(DEVIL)
			user.set_room_temp('question', 'sixth')
	elif question == 'sixth':
		if text == locale_manager.get('rooms.default.usual.devil.phrase_18'):
			reply(locale_manager.get('rooms.default.usual.devil.phrase_19'), photo='BQADAgADEQkAAmrZzgd_oBozeMUUGAI')
			user.set_room_temp('question', 'seventh')
	elif question == 'seventh':
		if text == locale_manager.get('rooms.default.usual.devil.phrase_20'):
			reply(' — Замечательно! А теперь мне пора вернуться к работе, а ты можешь идти и покорять мир!\nУ тебя в руках остался контракт, вглядевшись, ты видишь цифру 7...\n — Дай сюда! Он тебе не нужен.')
			user.leave(reply)

def get_actions(user):
	question = user.get_room_temp('question', def_val='first')
	ans = [ ]

	if question == 'first':
		ans = [ locale_manager.get('rooms.default.usual.devil.phrase_21'), locale_manager.get('rooms.default.usual.devil.phrase_22'), locale_manager.get('rooms.default.usual.devil.phrase_23') ]
	elif question == 'second':
		ans = [ locale_manager.get('rooms.default.usual.devil.phrase_24'), locale_manager.get('rooms.default.usual.devil.phrase_25') ]
	elif question == 'third':
		ans = [ locale_manager.get('rooms.default.usual.devil.phrase_26'), locale_manager.get('rooms.default.usual.devil.phrase_27'), locale_manager.get('rooms.default.usual.devil.phrase_28') ]
	elif question == 'forth':
		ans = [ locale_manager.get('rooms.default.usual.devil.phrase_29'), locale_manager.get('rooms.default.usual.devil.phrase_30') ]
	elif question == 'fifth':
		ans = [ locale_manager.get('rooms.default.usual.devil.phrase_31'), locale_manager.get('rooms.default.usual.devil.phrase_32'), locale_manager.get('rooms.default.usual.devil.phrase_33'), 'Я хочу всё!' ]
	elif question == 'sixth':
		ans = [ locale_manager.get('rooms.default.usual.devil.phrase_34') ]
	elif question == 'seventh':
		ans = [ locale_manager.get('rooms.default.usual.devil.phrase_35') ]

	return ans
