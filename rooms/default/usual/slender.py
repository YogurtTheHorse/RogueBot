from constants import *

READY = 'Войти в туман'
ESCAPE = 'Уйти'

name = 'Туман'

def enter(user, reply):
	reply('Ты ничего не видишь, здесь все в тумане.', photo=FOG_STICKER)
	user.set_room_temp('question', 'first')

def action(user,reply, text):
	question = user.get_room_temp('question', def_val='first')

	if question == 'first':
		if text == READY:
			reply('Войдя в туман, ты обнаруживаешь, что дверь за тобой исчезла. Ты продолжаешь идти вперед, постепенно туман расступается, обнажая стволы деревьев.\nТы в лесу.\nГуляя по лесу ты замечаешь что на одном из деревьев закреплен листок бумаги.')
			user.set_room_temp('question', 'second')
		else:
			reply('Дверь за тобой с силой захлопнулась.')
			user.leave(reply)
	elif question == 'second':
		if text == 'Сорвать':
			reply('Ты снимаешь листок с дерева и осматриваешь. На обратной стороне ты замечаешь надпись крупными буквами:\nВСЕГДА СМОТРИТ. НЕТ ГЛАЗ.\n1/4\nГде-то вдалеке ты слышишь шум.')
			user.set_room_temp('question', 'third')
	elif question == 'third':
		if text == 'Идти на шум':
			reply('Шум усиливается, внезапно из-за деревьев возник неестественно высокий человек.\nТы не можешь двигаться.\nТьма окутала твоё сознание.', photo='BQADAgAD4AgAAmrZzgdmsBNDB5hPiQI')
			user.death(reply, reason='Слендер')
		else:
			reply('Ты бежишь, постепенно шум утихает. Ты осматриваешься и замечаешь что находишься на границе леса.\nВдалеке виднеется водонапорная вышка, парк трейлеров и какой-то ангар, но дорога есть только к вышке.')
			user.set_room_temp('question', 'forth')
	elif question == 'forth':
		if text == 'Идти к вышке':
			reply('Ты подошел к вышке. Осмотрев ее, ты обнаруживаешь на одной из опор еще один лист бумаги.\nНа обратной стороне рисунок человека с неестественно длинными конечностями и текст:\nНЕТ НЕТ НЕТ НЕТ НЕТ НЕТ НЕТ НЕТ.\n2/4\nТы снова слишишь шум, но в этот раз ближе и громче.')
			user.set_room_temp('question', 'fifth')
	elif question =='fifth':
		if text == 'Бежать':
			reply('Ты приближаешься к ангару.\nШум утих.')
			user.set_room_temp('question', 'seventh')
		else:
			reply('Ты поворачиваешься на шум и видишь вдалеке медленно движущегося к вам человека.\nНет, не человека, это существо мало похоже на него. Всмотревшись, ты замечаешь, что у него слишком длинные конечности.\nТы скован ужасом, но действовать надо быстро.\nПрятаться тут негде, так что придется бежать.', photo='BQADAgAD4AgAAmrZzgdmsBNDB5hPiQI')
			user.set_room_temp('question', 'sixth')
	elif question == 'sixth':
		if text == 'Бежать':
			reply('Ты приближаешься к ангару. Ты оторвался от монстра.\nШум утих.')
			user.set_room_temp('question', 'seventh')
	elif question == 'seventh':
		if text == 'Войти внутрь':
			reply('Внутри Ты видишь тускло мерцающую лампу, стол и опрокинутый стул.\nПодойдя к столу ты видишь бутылку с какой-то жидкостью, наполовину полный стакан и очередной лист бумаги.')
			user.set_room_temp('question', 'eighth')
	elif question == 'eighth':
		if text == 'Посмотреть лист':
			reply('Взяв в руки лист бумаги ты обнаруживаешь на другой стороне надпись :\nНЕ СМОТРИ....\nИЛИ ОН ЗАБЕРЕТ ТЕБЯ.\n3/4\nПрочитав этот текст ты вновь услышал шум.')
			user.set_room_temp('question', 'nineth')
	elif question == 'nineth':
		if text == 'Выбежать из ангара':
			reply('Выбежав из ангара, ты столкнулся с ним лицом к лицу.\nТьма окутала твоё сознание', photo='BQADAgAD4AgAAmrZzgdmsBNDB5hPiQI')
			user.death(reply, reason='Слендер')
		else:
			reply('Ты прячешься под столом. Странно, но это сработало, шум утих.')
			user.set_room_temp('question', 'tenth')
	elif question == 'tenth':
		if text == 'Выйти из ангара':
			reply('Ты вышел из ангара и снова услышали шум, здесь оставаться небезопасно.')
			user.set_room_temp('question', 'eleventh')
	elif question == 'eleventh':
		if text == 'Бежать к трейлерам':
			reply('Пока ты идешь к трейлерам, шум усиливается и теперь раздается из-за вашей спины.')
			user.set_room_temp('question', 'dozenth')
	elif question == 'dozenth':
		if text == 'Обернуться':
			reply('Это было глупо.\nТьма окутала твоё сознание.')
			user.death(reply, reason='Слендер')
		else:
			reply('Ты добегаешь до трейлеров, шум ослаб, но не исчез. Осмотревшись, ты не видишь последнего рисунка, надо еще осмотреться.')
			user.set_room_temp('question', 'thirteenth')
	elif question == 'thirteenth':
		if text == 'Искать':
			reply('Шум стал громче, твоё сердцебиение участилось. Заглянув за очередной трейлер, ты обнаруживаешь скомканную бумажку. Развернув ее ты видишь большую надпись:\nНЕЛЬЗЯ УБЕЖАТЬ\n4/4\nТебя затрясло, ведь ты не понимаешь, как же так, все это было зря? Но твои размышления прервал усилившийся шум.')
			user.set_room_temp('question', 'fourteenth')
	elif question == 'fourteenth':
		if text == 'Бежать':
			reply('Ты спотыкаешься и падаешь. Источник шума совсем рядом. Быстрее!')
			user.set_room_temp('question', 'fifteenth')
	elif question == 'fifteenth':
		if text == 'Откатиться под трейлер':
			reply('Ты лежишь под трейлером. Шум стал невыносимо громким. Из своего укрытия ты видишь две тонкие ноги, которые проходят мимо, смотря на них, ты замечаешь дверь в отдалении...')
			user.set_room_temp('question', 'sixteenth')	
	elif question == 'sixteenth':
		if text == 'Бежать к двери':
			reply('Ты же не думал, что получится?\nТьма окутала твоё сознание.')
			user.death(reply, reason='Слендер')
		else:
			reply('Ты заметил, как ноги остановились вдалеке от двери. У тебя есть шанс!')
			user.set_room_temp('question', 'seventeenth')
	elif question == 'seventeenth':
		if text == 'Бежать к двери':
			reply('Ты захлопываешь за собой дверь и слышишь глухие удары с другой стороны. Надо убираться отсюда.\nРядом с дверью ты обнаруживаешь 100 золотых')
			user.gold += 100
			user.leave(reply)

def get_actions(user):
	question = user.get_room_temp('question', def_val='first')
	ans = [ ]

	if question == 'first':
		ans = [ READY, ESCAPE ]
	elif question == 'second':
		ans = [ 'Сорвать' ]
	elif question == 'third':
		ans = [ 'Идти на шум', 'Бежать' ]
	elif question == 'forth':
		ans = [ 'Идти к вышке' ]
	elif question == 'fifth':
		ans = [ 'Бежать', 'Посмотреть в сторону шума' ]
	elif question == 'sixth':
		ans = [ 'Бежать' ]
	elif question == 'seventh':
		ans = [ 'Войти внутрь' ]
	elif question == 'eighth':
		ans = [ 'Посмотреть лист' ]
	elif question == 'nineth':
		ans = [ 'Выбежать из ангара', 'Спрятаться под столом' ]
	elif question == 'tenth':
		ans = [ 'Выйти из ангара' ]
	elif question == 'eleventh':
		ans = [ 'Бежать к трейлерам' ]
	elif question == 'dozenth':
		ans = [ 'Обернуться', 'Не оборачиваться' ]
	elif question == 'thirteenth':
		ans = [ 'Искать' ]
	elif question == 'fourteenth':
		ans = [ 'Бежать' ]
	elif question == 'fifteenth':
		ans = [ 'Откатиться под трейлер' ]
	elif question == 'sixteenth':
		ans = [ 'Бежать к двери', 'Подождать' ]
	else:
		ans = [ 'Бежать к двери' ]

	return ans
