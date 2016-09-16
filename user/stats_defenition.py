from localizations import locale_manager

def debug_info(self):
	msg = 'uid: ' + str(self.uid) + '\n'
	msg += 'name: ' + str(self.name) + '\n'
	msg += 'hp: ' + str(self.hp) + '\n'
	msg += 'mp: ' + str(self.mp) + '\n'
	msg += 'pet: ' + str(self.pet) + '\n'
	msg += 'gold: ' + str(self.gold) + '\n'
	msg += 'max_hp: ' + str(self.max_hp) + '\n'
	msg += 'max_mp: ' + str(self.max_mp) + '\n'
	msg += 'state: ' + str(self.state) + '\n'
	msg += 'inventory_page: ' + str(self.inventory_page) + '\n'
	msg += 'gods: ' + str(self.gods) + '\n'
	msg += 'gods_level: ' + str(self.gods_level) + '\n'
	msg += 'gods: ' + str(self.gods) + '\n'
	msg += 'last_god: ' + str(self.last_god) + '\n'
	msg += 'prayed: ' + str(self.prayed) + '\n'
	msg += 'damage: ' + str(self.damage) + '\n'
	msg += 'defence: ' + str(self.defence) + '\n'
	msg += 'charisma: ' + str(self.charisma) + '\n'
	msg += 'mana_damage: ' + str(self.mana_damage) + '\n'
	msg += 'visited_shop: ' + str(self.visited_shop) + '\n'
	msg += 'shop_items: ' + str(self.shop_items) + '\n'
	msg += 'shop_names: ' + str(self.shop_names) + '\n'
	msg += 'tags: ' + str(self.tags) + '\n'
	msg += 'room: ' + str(self.room) + '\n'
	msg += 'room_temp: ' + str(self.room_temp) + '\n'
	msg += 'reborn_answer: ' + str(self.reborn_answer) + '\n'
	msg += 'dead: ' + str(self.dead) + '\n'
	msg += 'subject: ' + str(self.subject) + '\n'
	msg += 'variables: ' + str(self.variables) + '\n'
	msg += 'buffs: ' + str(self.buffs) + '\n'
	msg += 'missions: ' + str(self.missions)

	return msg

def get_gold_bonus(self):
	res = 1
	for i in self.get_active_items():
		res *= i.gold_bonus

	for b in self.buffs:
		res *= b.gold_bonus

	if self.pet:
		res *= self.get_pet().gold_bonus

	return res

def get_damage(self):
	res = 0
	for i in self.get_active_items():
		res += i.damage

	if self.pet:
		res += self.get_pet().damage

	return res + self.damage

def get_damage_bonus(self, reply):
	res = 0
	for i in self.get_active_items():
		res += i.get_damage_bonus(self, reply)

	for b in self.buffs:
		res += b.damage_plus

	if self.pet:
		res += self.get_pet().get_damage_bonus(self, reply)

	return res

def get_defence(self):
	res = 0
	for i in self.get_active_items():
		res += i.defence

	for b in self.buffs:
		res += b.defence

	if self.pet:
		res += self.get_pet().defence

	return res + self.defence

def get_charisma(self):
	res = 0
	for i in self.get_active_items():
		res += i.charisma

	for b in self.buffs:
		res += b.charisma

	if self.pet:
		res += self.get_pet().charisma

	return res + self.charisma

def get_mana_damage(self):
	res = 0
	for i in self.get_active_items():
		res += i.mana_damage

	for b in self.buffs:
		res += b.mana_damage_plus

	if self.pet:
		res += self.get_pet().mana_damage

	return res + self.mana_damage

def has_aura(self, aura):
	for i in self.get_active_items():
		if i.aura == aura:
			return True
			
	return False

def use_mana(self, mp):	
	if self.mp >= mp:
		self.mp -= mp
		return True
	
	return False

def heal(self, hp):
	self.hp = min(self.hp + hp, self.max_hp)

def mana(self, mp):
	self.mp = min(self.mp + mp, self.max_mp)

def get_stats(self):
	return locale_manager.get('USER_STATS').format(self.hp, self.mp, self.gold)

def add_tag(self, tag):
	self.tags.append(tag)

def has_tag(self, tag):
	if tag in self.tags:
		return True

	#for i in self.get_items():
	#	if tag in i.tags:
	#		return True

	return False

def remove_tag(self, tag):
	self.tags.remove(tag)

def show_characteristics(self, reply):
	msg = locale_manager.get('CHARACTERISTICS').format(
		self.get_damage(), 
		self.get_defence(), 
		self.get_charisma(),
		self.get_mana_damage(),
		self.monsters_killed,
		self.rooms_count
	)

	reply(msg)
	self.open_corridor(reply)

def set_variable(self, name, val=None):
	self.variables[name] = val

def get_variable(self, name, def_val=None):
	if name in self.variables:
		return self.variables[name]
	else:
		return def_val

def new_buff(self, buff):
	self.buffs.append(buff)
