class Buff(object):
	def __init__(self, time, defence=0, damage_plus=0, mana_damage_plus=0, heal=0, damage=0, charisma=0):
		super(Buff, self).__init__()
		self.time = time
		self.defence = defence
		self.damage_plus = damage_plus
		self.mana_damage_plus = mana_damage_plus
		self.heal = heal
		self.damage = damage
		self.charisma = charisma

	def on_room(self, user, reply, room):
		self.time -= 1
		
class RainbowBuff(Buff):
	def __init__(self):
		super(RainbowBuff, self).__init__(50, mana_damage_plus=50)
		