import random

name = 'Армия Вьетнамцев'

hp = 1500
damage_range =  ( 40, 70 )

coins = 1337

loot = [random.choice([ 'ak', 'm79' ])]

def enter(user, reply):
	msg = (
		'Огромая куча вьетнамцев, на летающих тракторах производства СССР, устроит дискотеку с фейерверком и светомузыкой. '
	)
	reply(msg, photo='BQADAgAD3AgAAmrZzgcgvL7Zlof8MQI')
