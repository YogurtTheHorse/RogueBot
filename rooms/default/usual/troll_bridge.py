from constants import *
import random

name = 'Мост'

c_PRICE             = 75        # Стоимость прохода 
c_MIN_ROOM_COUNT    = 200       # Мин комнат
c_MIN_STRENGTH_ANSW = 100       # Мин силы для нападения
c_MIN_INTELL_ANSW   = 100       # Мин интелекта для ответа
c_TROLL_R1          = 'Вы видите огромного тролля. Часть его лица покрыта мхом, остальную украшают множество шрамов. На голове у него советская каска со звездой.\n\n — Через этот мост просто так не ходят! Плати {} или обед!'.format(c_PRICE)
c_TROLL_R2          = ' — О привет боец. Не узнал сразу. Ты давай иди... Иди.'

GO     = 'Пройти через мост'
LEAVE  = 'Пройти мимо'
ESCAPE = 'Попытаться вырваться и убежать'
GUP    = 'Сдаться'
PAY    = 'Заплатить 75 золотых'
EAT    = 'Обед?!'
FIGHT  = 'Напасть!'
CHEAT  = 'Служу Советскому Союзу!'

def enter(user, reply):
	msg = (
		'Обычный такой мост. Через самую обычную реку.'
	)
	reply(msg, photo='BQADAgAD2wgAAmrZzgdIlwyFp4vXPwI')
	user.set_room_temp('question', 'first')

def dice(user, reply, result, subject=None):
	if subject == ESCAPE:
		if  result > (DICE_MAX / 4) * 3:
			reply('Вы сумели вырвать свою лодыжку из на секунду ослабшей хватки. Нога побаливает, но вы на свободе!')
			user.make_damage(10,15,reply)
			user.leave(reply)
		elif result < DICE_MAX / 4:
			reply('Удача отвернулась от Вас. В попытке вырваться Вы умудрились удариться головой об мост и умереть.')
			user.death(reply, reason=name)
		else:
			reply('Попытка вырваться была бесполезной. Вы под мостом.')
			if user.has_item('sunion_helmet'):
				reply(c_TROLL_R2)
				user.leave(reply)
			else:
				reply(c_TROLL_R1)
				user.set_room_temp('question','underbridge')
	elif subject == FIGHT:
		if  result > (DICE_MAX / 5) * 4:
			reply('Ловким ударом вы сбили каску троллю на глаза. Второй окончательно отправил монстра в мир снов.')
			reply('Вы нашли немного денег и забрали каску.')
			user.add_item('loot','sunion_helmet')
			user.give_gold(random.randrange(5,100,5))
			user.leave(reply)
		else:
			reply('Зря вы так поверили в свои силы. Драться с троллем — та еще затея.')
			user.death(reply, reason=name)


def action(user, reply, text):
	question = user.get_room_temp('question',def_val='first')

	if question == 'first':
		if text == GO:
			if user.rooms_count < c_MIN_ROOM_COUNT:                      
				reply('Проходя по мосту вы нашли золотую монетку.')
				user.add_item('neutral','coin')
				user.leave(reply)
			else:
				reply('Огромная лапа схватила вас за ногу и тянет под мост.')
				user.set_room_temp('question','scarryhand')
		elif text == LEAVE:
			reply('Вы прошли мимо.')
			user.leave(reply)
	elif question == 'scarryhand':
			if text == GUP: 
				reply('Вы под мостом.')
				if user.has_item('sunion_helmet'):
					reply(c_TROLL_R2)
					user.leave(reply)
				else:
					reply(c_TROLL_R1)
					user.set_room_temp('question','underbridge')
			elif text == ESCAPE:
				user.throw_dice(reply, ESCAPE)
	elif question == 'underbridge':
			if text == FIGHT:
				user.throw_dice(reply, FIGHT)
			elif text == PAY:
				if user.paid(c_PRICE):
					reply('Тролль отпустил вас.')
				else:
					reply('Ввиду отсутвия у вас необходимой суммы, Тролль хорошенько намял Вам бока, перед тем как отпустить.')
					user.make_damage(40,70,reply,name=name)
				user.leave(reply)
			elif text == EAT:
				reply('Тролль был очень рад, что Вы решили его накормить. Жаль только пообедал он вами.')
				user.death(reply, reason=name)
			elif text == CHEAT:
				reply(' — Молодец боец. Аккуратней ходить нужно. Вот держи каску, береги голову.')
				user.add_item('loot','sunion_helmet')
				user.leave(reply)

def get_actions(user):
	question  = user.get_room_temp('question',def_val='first')
	answers = []

	if question == 'first':
		answers = [ GO, LEAVE ]
	if question == 'scarryhand':
		answers = [ GUP, ESCAPE ]
	if question == 'underbridge':
		answers = [ PAY, EAT ]
		if user.damage >= c_MIN_STRENGTH_ANSW:
			answers += [ FIGHT ]
		if user.mana_damage >= c_MIN_INTELL_ANSW:
			answers += [ CHEAT ]
	random.shuffle(answers)
	return answers
