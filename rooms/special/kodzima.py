import random
import usermanager
from constants import *

HOW = '—А... э-э... как Вы здесь оказались?'
JOKE = 'Рассказать анекдот'
ASK = 'Могу я задать Вам один вопрос?...'

ANYTHING_ELSE = '—Есть ли что-нибудь вне этой бесконечной череды комнат?'
SLIME = '—Правда ли, что Вы лично приложили руку к разработке дизайна Слизня?'

BRAINSTORM = 'Пораскинуть мозгами'
TAKE_SPOON = 'Взять ложку'

name = 'Человек'

def enter(user, reply):
	msg = (
		'—Проходи, {0}, чего хотел?\n\nНа негнущихся коленях ты проходишь '
		'в середину комнаты. Да, глаза не подвели, это действительно...\n\n'
		'*Хидэо Кодзима*!'
	)
	reply(msg.format(user.name))
	user.set_room_temp('question', 'first')

def action(user, reply, text):
	question = user.get_room_temp('question', def_val='first')

	if question == 'first':
		if text == HOW:
			user1 = usermanager.random_user()
			user2 = usermanager.random_user()
			name1 = user1.name
			name2 = user2.name

			reply('—Так же, как и ты, очевидно же. Всё, не занимай линию, там за тобой уже двое в очереди. {0} и {1}, чёрт бы его побрал, уже третий раз за сегодня'.format(name1, name2))

			reply('Тебя выставили за дверь.')
			user.leave(reply)
		elif text == ASK:
			reply('—Только один.', photo=KODZIMA_STICKER)
			user.set_room_temp('question', 'question')
		else:
			reply('От волнения Вы не придумали ничего лучше, как рассказать анекдот собственного сочинения.\n—Заходит как-то геймдизайнер в бар, \n—бодро начинаете Вы, но неожиданно с Вашим лицом резко стыкуется табурет, на котором недавно сидел Хидэо:—Пошёл вон!')
			user.make_damage(25, 50, reply, False)

			reply('Тебя выставили за дверь.')
			user.leave(reply)
	elif question == 'question':
		if text == ANYTHING_ELSE:
			msg = (
				'—Ахаха. АХАХАХА. Насмешил, юродивый. Пораскинь мозгами, если коридор бесконечен,'
				' то место, где он находится, должно быть *больше, чем бесконечность*. Ты ещё '
				'скажи, что где-то существует огромная яркая жёлтая штука над головой и мы всего '
				'лишь записаны в память машины, размером меньше сундука, ахаха.  Вот, держи ложку и '
				'поменьше думай про всякую чушь.'
			)
			reply(msg)
			user.set_room_temp('question', 'spoon')
		else:
			msg = (
				'—Это долгая история... В те времена, когда я и  Гейб ещё не были совращены лёгкими '
				'деньгами, текущими золотой рекой из кошельков родителей школьников, мы сидели в '
				'гараже и размышляли. Я пил какао, а он, как обычно, ел курочку. И тут меня словно '
				'озарило: «Габе, как ты думаешь, есть ли такое существо, которым можно описать '
				'человеческое существование?». Начался жаркий спор, в ходе которого и родился '
				'прообраз Слизня, сидящего в комнате, и ждущего когда его раздавит кто-то вроде тебя, {0}.'
			)
			reply(msg.format(user.name))
			user.set_room_temp('question', 'slime')
	elif question == 'slime':
		reply(
			'—Вот же глупенький. В Слизне заключены четыре экзистенциальные данности:'
			'\n1. Смерть\n2. Свобода воли\n3. Одиночество\n4. Бессмысленность\n\n'
			'За сим прощаюсь, моя смена заканчивается. Надеюсь, эта информация '
			'не сведёт тебя с ума.Ты мне даже понравился. Вот держи, на память.'
		)
		user.add_item('special', 'spoilers')
		user.leave(reply)
	elif question == 'spoon':
		if text == BRAINSTORM:
			reply('Ты перестарался и мозги раскинулись по всей комнате. ')
			user.death(reply, reason='Повышенная умственная активность')
		else:
			reply('Получена Серебрянная ложка')
			user.add_item('special', 'good_spoon')
			user.leave(reply)



def get_actions(user):
	question = user.get_room_temp('question', def_val='first')
	ans = [ ]

	if question == 'first':
		if user.get_mana_damage() < 7:
			ans = [ HOW, JOKE ]
		else:
			ans = [ ASK ]
	elif question == 'question':
		ans = [ ANYTHING_ELSE, SLIME ]
	elif question == 'spoon':
		return [ BRAINSTORM, TAKE_SPOON ]
	elif question == 'slime':
		ans = [ 'Не понимаю... Слизень... И человеческое существование...' ]
	else:
		ans = [ 'Загрузка' ]

	return ans
