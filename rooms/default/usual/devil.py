from constants import *
from utils.buffs import DevilPower
from utils.buffs import DevilInt
from utils.buffs import DevilMoney
from utils.buffs import DevilEntity

name = 'Уютная комната'

def enter(user, reply):
	reply('Ты видишь просторную комнату.\nВ углу тихо потрескивает камин, на стенах развешаны охотничьи трофеи.\nЗдесь довольно уютно.\nЧуть погодя, твои глаза привыкли к полумраку царящему в комнате и ты замечаешь человека за столом. Он поглощен работой, постоянно что-то сверяет на разных листах бумаги. Как он это делает в такой темноте?', photo='BQADAgADEgkAAmrZzgeGC93mbCR4mwI')
	user.set_room_temp('question', 'first')

def action(user, reply, text):
	question = user.get_room_temp('question', def_val='first')
	MADE_SOLUTION_TEXT = 'Отличный выбор, а теперь подпиши здесь и вот здесь.\nПеред вами возник исписанный на непонятном языке пергамент с двумя галочками.\n — Ну же, условия стандартные: когда умрешь я заберу твою душу.'
	CURSE_TEXT = ' изменился в лице, кажется ему не понравилось это. — Тогда вот тебе маленький подарок, чтобы ты знал, что не нужно отрывать меня от работы по пустякам.'

	if question == 'first':
		if text == 'Кашлянуть':
			reply('Это не возымело никакого эффекта.')
		elif text == 'Подойти к столу':
			reply('Ты подходишь вплотную к столу. Человек отрывается от бумаг, поправляет очки и выжидательно смотрит на тебя.')
			user.set_room_temp('question', 'second')
		else:
			reply('На тебя не обратили внимания и ты ушёл.')
			user.leave(reply)
	elif question == 'second':
		if text == 'Я пойду, пожалуй':
			reply('Человек ухмыляется и возвращается к работе.')
			user.leave(reply)
		elif text == 'Кто вы?':
			usr_name = user.name.lower()
			reply('У меня много имен, {0}. В разных культурах меня называли по-разному. Я помогал людям добиться превосходных результатов, начинал войны, насылал болезни.'.format(usr_name))
			user.set_room_temp('question', 'third')
	elif question == 'third':
		if text == 'Я пойду, пожалуй':
			reply('Человек {0}'.format(CURSE_TEXT))
			user.max_hp -= 50
			user.leave(reply)
		elif text == 'Вы дьявол?':
			reply('Человек рассмеялся. — Ну зачем сразу так грубо? Возможно это и одно из моих имен, но точно не самое любимое. Все что тебе нужно знать, это то, что я твой друг. Ну, чего ты хочешь?')
			user.set_room_temp('question', 'forth')
		else:
			reply('Внезапно он исчез из виду и вы услышали шепот у себя в голове\n — Может ты хочешь бесконечную силу, чтобы все трепетали пред тобой?\nИли ты хочешь быть гением, способным на всё?\nХотя нет, наверное, ты хочешь несметного богатства?\nИли же всё сразу?\nВыбирай, смертный!')
			user.set_room_temp('question', 'fifth')
	elif question == 'forth':
		if text == 'Я пойду, пожалуй':
			reply('Дьявол {0}'.format(CURSE_TEXT))
			user.max_hp -= 50
			user.leave(reply)
		elif text == 'А что ты предложишь мне?':
			reply('Внезапно он исчез из виду и вы услышали шепот у себя в голове\n — Может ты хочешь бесконечную силу, чтобы все трепетали пред тобой?\nИли ты хочешь быть гением, способным на всё?\nХотя нет, наверное, ты хочешь несметного богатства?\nИли же всё сразу?\nВыбирай, смертный!')
			user.set_room_temp('question', 'fifth')
	elif question == 'fifth':
		if text == 'Силу!':
			reply(MADE_SOLUTION_TEXT)
			user.new_buff(DevilPower())
			user.add_tag(DEVIL)
			user.set_room_temp('question', 'sixth')
		elif text == 'Знания!':
			reply(MADE_SOLUTION_TEXT)
			user.new_buff(DevilInt())
			user.add_tag(DEVIL)
			user.set_room_temp('question', 'sixth')
		elif text == 'Деньги!':
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
		if text == 'А когда я умру?':
			reply('У дьявола сверкнули глаза.\n — Увы этого никто не знает, даже я.', photo='BQADAgADEQkAAmrZzgd_oBozeMUUGAI')
			user.set_room_temp('question', 'seventh')
	elif question == 'seventh':
		if text == 'Подписать':
			reply(' — Замечательно! А теперь мне пора вернуться к работе, а ты можешь идти и покорять мир!\nУ тебя в руках остался контракт, вглядевшись, ты видишь цифру 7...\n — Дай сюда! Он тебе не нужен.')
			user.leave(reply)

def get_actions(user):
	question = user.get_room_temp('question', def_val='first')
	ans = [ ]

	if question == 'first':
		ans = [ 'Кашлянуть', 'Подойти к столу', 'Уйти' ]
	elif question == 'second':
		ans = [ 'Я пойду, пожалуй', 'Кто вы?' ]
	elif question == 'third':
		ans = [ 'Я пойду, пожалуй', 'Вы дьявол?', 'А что ты предложишь мне?' ]
	elif question == 'forth':
		ans = [ 'Я пойду, пожалуй', 'А что ты предложишь мне?' ]
	elif question == 'fifth':
		ans = [ 'Силу!', 'Знания!', 'Деньги!', 'Я хочу всё!' ]
	elif question == 'sixth':
		ans = [ 'А когда я умру?' ]
	elif question == 'seventh':
		ans = [ 'Подписать' ]

	return ans
