import random
from constants import *

EVIL_COMISSAR = 'EVIL_COMISSAR'

READY = 'Сказать, что готовы'
ESCAPE = 'Попытаться убежать'
FIGHT = 'Напасть на комиссара.'

name = 'Комиссар'

def enter(user, reply):
	msg = (
		'Не знаю, кто это такой, но он в форме, похожей на немецкую, '
		'и с двухглавым орлом на фуражке. В углу вы замечаете множество '
		'трупов с простреленной головой...\n\nОн говорит вам: «О, новобранец. '
		'Я думал, в этом мире-улье никто не хочет служить. Сейчас будет '
		'небольшой опрос на определение твоего отряда. Бояться нечего»'
	)
	reply(msg, photo='BQADAgADHwEAAgy18wMAAWs-pH_tD3MC')
	user.set_room_temp('question', 'first')

def dice(user, reply, result, subject=None):
	if subject == ESCAPE:
		if result > (DICE_MAX / 3) * 2:
			reply('Ты сбежал без потерь.')
			user.make_damage(10, 20, reply, name=name)
			user.leave(reply)
		elif result > DICE_MAX / 3:
			reply('Подстрелили руку. Держись, борец')
			user.make_damage(10, 20, reply)
			user.leave(reply)
		else:
			reply('Да вас, батенька, расстреляли')
			user.death(reply, reason=name)
	elif subject == FIGHT:
		if result > DICE_MIDDLE:
			reply('Победа за тобой. НО комиссар тебе это припомнит')
			user.add_tag(EVIL_COMISSAR)
			user.add_item('loot', 'laser_gun')
			user.leave(reply)
		else:
			reply('Да вас, батенька, расстреляли')
			user.death(reply, reason=name)

def action(user, reply, text):
	question = user.get_room_temp('question', def_val='first')

	if question == 'first':
		if text == READY:
			reply('Ну хорошо. Боец, ты моешься вообще? А то тут чем-то пахнет.')
			user.set_room_temp('question', 'smell')
		elif text == ESCAPE:
			reply('Комиссар начал кричать что-то про предателя и бегство. Время кидать кубики!')
			user.throw_dice(reply, ESCAPE)
		elif text == FIGHT:
			reply('В атаку!')
			user.throw_dice(reply, FIGHT)
	elif question == 'smell':
		if text == 'Да':
			reply('А, ну да, я забыл про те трупы в углу. Надо будет сжечь их как-нибудь на досуге... Ну ладно, первый вопрос. Умеешь колдовать? Нам в Гвардии нужны маги.')
			user.set_room_temp('question', 'mage')
		else:
			reply('Последователь Нургла! Расстрелять!')
			reply('Придется бежать')

			user.throw_dice(reply, ESCAPE)
	elif question == 'mage':
		if text == 'Да':
			reply('Последователь Тзинча! Расстрелять!')
			reply('Бежим быстрее')

			user.throw_dice(reply, ESCAPE)
		else:
			reply('Ну конечно, не умеешь, ведь магия - это ересь, верно, боец?')
			reply('На стене вы замечаете плакат с женщиной, похоже, эльфийкой. У неё большой размер груди, и одета она очень откровенно... Комиссар ехидно улыбается и говорит:')

			reply('О, вижу, ты заметил мой плакатик. Ну и как тебе? Понравилась, да?')

			user.set_room_temp('question', 'poster')
	elif question == 'poster':
		if text == 'Нет':
			reply('Комиссар меняет улыбку на серьезное выражение лица. "Ну конечно, нет, это же ксенос. Неизвестно, что еще у него там в шта... кхм. Говорю, это от предыдущего владельца комнаты осталось.')
			reply('Кажется, ты прошел все испытания. Но у нас пока нет мест, ты приходи лет через 20, когда мы на следующую планету соберемся, ладно? А теперь иди отсюда, мне еще тела убрать надо. Славься Император!')

			for i in range(7):
				user.add_item('neutral', 'laser_bullet')
			user.leave(reply)
		else:
			reply('Комиссар резко изменяется в лице и орет на тебя: "Ну это вообще беспредел! Мало того, что ксеносов не ненавидят, еще и слаанешизм развели какой-то! Расстрелять!')
			reply('Время спасаться!')

			user.throw_dice(reply, ESCAPE)

def get_actions(user):
	question = user.get_room_temp('question', def_val='first')
	ans = [ ]

	if question == 'first':
		ans = [ READY, ESCAPE, FIGHT ]
	elif question == 'smell' or question == 'mage':
		ans = [ 'Да', 'Нет' ]
	else:
		ans = [ 'Черт возьми, ДА!', 'Нет' ]

	random.shuffle(ans)

	return ans