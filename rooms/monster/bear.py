name = 'Медведь'

hp = 70
damage_range =  ( 15, 30 )

coins = 50

loot = [ ]

def enter(user, reply):
	reply('Огромный медведь рычит на тебя.')

	if user.has_item('fish') or user.has_item('honey'):
		user.remove_item('fish')
		user.remove_item('honey')

		user.new_pet(reply, 'bear')
