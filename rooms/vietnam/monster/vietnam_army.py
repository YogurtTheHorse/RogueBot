from localizations import locale_manager
import random

name = locale_manager.get('rooms.vietnam.monster.vietnam_army.phrase_1')

hp = 1500
damage_range =  ( 40, 70 )

coins = 1337

loot = [random.choice([ 'ak', 'm79' ])]

def enter(user, reply):
	msg = (
		locale_manager.get('rooms.vietnam.monster.vietnam_army.phrase_2'))
	reply(msg, photo='BQADAgAD3AgAAmrZzgcgvL7Zlof8MQI')
