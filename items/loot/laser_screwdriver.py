from localizations import locale_manager
import databasemanager

name = locale_manager.get('items.loot.laser_screwdriver.phrase_1')
description = locale_manager.get('items.loot.laser_screwdriver.phrase_2')
price = 1000

defence = 100
damage = 100
mana_damage = 100

fightable = True

def on_room(user, reply, room):
	name = databasemanager.get_variable('doctor_killer')
	if user.name != name:
		reply(locale_manager.get('items.loot.laser_screwdriver.phrase_3'))
		user.remove_item('laser_screwdriver')

def fight_use(user, reply, room):
	reply(locale_manager.get('items.loot.laser_screwdriver.phrase_4'))
	return 0