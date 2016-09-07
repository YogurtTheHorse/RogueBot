import copy
import usermanager

def save(self):
	save = dict()

	save['hp'] = copy.copy(self.hp)
	save['mp'] = copy.copy(self.mp)
	save['gold'] = copy.copy(self.gold)
	save['race'] = copy.copy(self.race)

	save['max_hp'] = copy.copy(self.max_hp)
	save['max_mp'] = copy.copy(self.max_mp)


	save['items'] = copy.copy(self.items)
	save['active_items'] = copy.copy(self.active_items)
	save['inventory_page'] = copy.copy(self.inventory_page)

	save['gods'] = copy.copy(self.gods)
	save['gods_level'] = copy.copy(self.gods_level)
	save['last_god'] = copy.copy(self.last_god)
	save['prayed'] = copy.copy(self.prayed)

	save['damage'] = copy.copy(self.damage)
	save['defence'] = copy.copy(self.defence)
	save['charisma'] = copy.copy(self.charisma)
	save['mana_damage'] = copy.copy(self.mana_damage)

	save['tags'] = copy.copy(self.tags)

	save['reborn_answer'] = copy.copy(self.reborn_answer)

	save['rooms_to_story'] = copy.copy(self.rooms_to_story)
	save['next_story_room'] = copy.copy(self.next_story_room)
	save['story_level'] = copy.copy(self.story_level)

	save['last_message'] = copy.copy(self.last_message)
	save['rooms_count'] = copy.copy(self.rooms_count)
	save['monsters_killed'] = copy.copy(self.monsters_killed)

	save['variables'] = copy.copy(self.variables)
	save['pet'] = copy.copy(self.pet)

	self.set_variable('save', save)

def recover(self, reply):
	save = self.get_variable('save')

	try:
		self.hp = save['hp']
		self.mp = save['mp']
		self.gold = save['gold']
		self.race = save['race']

		self.max_hp = save['max_hp']
		self.max_mp = save['max_mp']


		self.items = save['items']
		self.active_items = save['active_items']
		self.inventory_page = save['inventory_page']

		self.gods = save['gods']
		self.gods_level = save['gods_level']
		self.last_god = save['last_god']
		self.prayed = save['prayed']

		self.damage = save['damage']
		self.defence = save['defence']
		self.charisma = save['charisma']
		self.mana_damage = save['mana_damage']

		self.tags = save['tags']

		self.reborn_answer = save['reborn_answer']

		self.rooms_to_story = save['rooms_to_story']
		self.next_story_room = save['next_story_room']
		self.story_level = save['story_level']

		self.last_message = save['last_message']
		self.rooms_count = save['rooms_count']
		self.monsters_killed = save['monsters_killed']

		self.variables = save['variables']
		self.pet = save['pet']

		self.state = 'corridor'
		self.subject = None

		self.room = ('', '')
		self.room_temp = { }

		self.dead = False
		self.visited_shop = False
		self.shop_items = [ ]
		self.shop_names = [ ]

		self.set_variable('save', None)

		usermanager.save_user(self)
	except:
		pass
	finally:
		reply('О, сохранение!')
		self.open_corridor(reply)