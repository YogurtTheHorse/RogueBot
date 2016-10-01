import tornamentmanager

name = 'Колизей'

def enter(user, reply):
	user.hp = user.max_hp
	tornament = tornamentmanager.get_tornament(user.tornament_id)
	names = ', '.join(tornament['names'])

	reply('Боги вылечили твои недуги и ниспослали в Колизей.')
	reply('Вместе с тобой тут находятся: {0}'.format(names))

def get_actions(user):
	return user.get_fight_actions()

def dice(user, reply, result, subject=None):
	return user.fight_dice(reply, result, subject)

def action(user, reply, text):
	user.fight_action(reply, text)

def make_damage(user, reply, dmg):
	tornamentmanager.make_damage(user, reply, dmg)