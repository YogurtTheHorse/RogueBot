from constants import *

name = 'Книга судьбы'

def enter(user, reply):
	reply('Потрёпанная книга посреди комнаты.\nОна лежит в луже воды.', photo=BOOK_FIRST_STICKER)
	user.set_room_temp('question', 'first')

def action(user, reply, text):
		question = user.get_room_temp('question', def_val='first')

		if question == 'first':
			if text == 'Перевернуть страницу':
				reply('Открыв первую страницу, ты отшатнулся от книги и чуть было не выронил ее из рук. От неё веет какой-то тёмной магией. Пересилив себя ты начинаешь читать первую страницу. местами буквы расплылись.\n\n«ВСRК, КТ0 П0СМЕЕТ\n(неразборчиво) RВИТСЯ\nЗО,^,ИАК П0 BЪДЕ, П0 3E,^^,ЛE,\nП0 СН/\М ЕГ0.»', photo=BOOK_SECOND_STICKER)
				user.set_room_temp('question', 'second')
				user.make_damage(10, 10, reply, name=name)
			else:
				user.leave(reply)
		elif question == 'second':
			if text == 'Перевернуть страницу':
				reply('На второй странице удалось разобрать лишь одно предложение:\n\n«НЕ 3РN В М0И ПNСAНИR\nКОЪДА ДИКNЙ КОТ НЕ В0ЕТ Н4\nЛYНУ»', photo=BOOK_THIRD_STICKER)
				user.set_room_temp('question', 'third')
				user.make_damage(10, 10, reply, name=name)
			else:
				user.leave(reply)
		elif question == 'third':
			if text == 'Перевернуть страницу':
				reply('|] ПЬОРОЧЕСТВОВАЛ .АРАП Д}ХУБА, СNRНNЕ В\nНЕ60СВО,^,Е, К0ТОР\n…\n(неразборчиво)\n…\nN ЯВNТСЯ ЗА ,^,YШАМИ, К0И ЕГО ВСЕ7ДА 6ЫЛN\nИ НЕ7 Т0ГО ВОNНА, 4ТО НЕ ПАДЕТ 0Т 3ГО\n}х{ЕСТА СМЪРТN»', photo=BOOK_FOURTH_STICKER)
				user.set_room_temp('question', 'forth')
				user.make_damage(10, 10, reply, name=name)
			else:
				user.leave(reply)
		elif question == 'forth':
			if text == 'Перевернуть страницу':
				reply('«3ВЪРЬ ЧТО ДАЪУЕТ\nУСЛА,^,У ГЛАЗY И П0х{ИР4ЕТ\nВСRКY ТВЪРЬ П0Л3YЧУ-.Ю\n…\nН3 0ТПУСКЪЙ\n…\nДОСМ0Т?»')
				user.set_room_temp('question', 'fifth')
				user.make_damage(10, 10, reply, name=name)
			else:
				user.leave(reply)
		elif question == 'fifth':
			reply('сМЪРТЬ', photo=BOOK_END_STICKER)
			user.death(reply, reason=name)		

def get_actions(user):
	question = user.get_room_temp('question', def_val='first')
	ans = [ ]

	return [ 'Перевернуть страницу', 'Уйти' ]
