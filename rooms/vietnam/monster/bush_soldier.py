name = 'Куст'
hp = 280
damage_range = (20, 35)

coins = 200

loot = [ 'm-16' ]

def enter(user, reply):
	reply('Когда ты проходил мимо куста, из него выпрыгнул солдат и ударил тебя прикладом', photo='BQADAgADDgkAAmrZzgf0VttBNllKWwI')
	user.make_damage(0, 30, reply, name='Приклад')
