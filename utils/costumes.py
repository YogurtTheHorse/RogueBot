import random

COSTUMES = {
	'mexican': {
		'who': 'Мексиканского рестлера',
		'description': 'Надевая костюм, ты почувствовал как кокс, оставшийся на одежде, попадает в твое тело и ты наполняешься силой.'
	}, 
	'ghost': {
		'who': 'Призрака',
		'description': 'Простыня все еще в моде!'
	}, 
	'sceleton': {
		'who': 'Скелета',
		'description': 'С чем стирать и материал не уточняются.. Но выглядят прямо как настоящие! Жуть.'
	},
	'fox': {
		'who': 'Лисички',
		'description': 'Этот хвост так интересно крепится!'
	}, 
	'headless': {
		'who': 'Всадника без головы',
		'description': 'Стало легче выпря	млять спину, но теперь ты видишь всё так, будто глаза на уровне пупка.'
	},
	'zombie': {
		'who': 'Зомби',
		'description': 'Весь в блювотине, но перфоманс того требует.'
	}, 
	'wizzard': {
		'who': 'Волшебника',
		'description': 'Колпак и палочка Гарри Поттера, которого избили и выкинули в канаву.'
	},
	'none': {
		'who': 'Самого себя',
		'description': 'Так себе конечно. Одел бы нижнее белье хотя бы'
	}
}

def rand_costume_key():
	return random.choice(list(COSTUMES))

def rand_costume():
	return get_costume(rand_costume_key())

def get_costume(key):
	if key in COSTUMES:
		return COSTUMES[key]
	else:
		return COSTUMES['none']