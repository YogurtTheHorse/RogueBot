from localizations import locale_manager
from constants import *
import random

class Buff(object):
	def __init__(self, time, name='buff', defence=0, damage_plus=0, mana_damage_plus=0, heal=0, damage=0, charisma=0, gold_bonus=1):
		super(Buff, self).__init__()
		self.time = time
		self.name = name
		self.defence = defence
		self.damage_plus = damage_plus
		self.mana_damage_plus = mana_damage_plus
		self.heal = heal
		self.damage = damage
		self.charisma = charisma
		self.gold_bonus = gold_bonus

	def get_name(self):
		try:
			return self.name
		except Exception:
			return 'buff'

	def on_room(self, user, reply, room):
		self.time -= 1

	def on_end(self, user, reply, room):
		pass

	def is_negative(self):
		return False
		
class RainbowBuff(Buff):
	def __init__(self):
		super(RainbowBuff, self).__init__(20, name='rainbow', mana_damage_plus=50)
		
class VietnamBuff(Buff):
	def __init__(self):
		super(VietnamBuff, self).__init__(100000, name='negative_vietnam')

	def on_room(self, user, reply, room):
		self.time -= 1
		self.make_damage(5, 5, reply, name=locale_manager.get('buffs.phrase_101'))
		reply(locale_manager.get('buffs.phrase_102'))

	def is_negative(self):
		return True
		
class NegativeRainbowBuff(Buff):
	def __init__(self):
		super(NegativeRainbowBuff, self).__init__(50, name='negative_rainbow', mana_damage_plus=50)

	def on_room(self, user, reply, room):
		self.time -= 1
		self.mana_damage_plus = (1.25 * random.random() - 1) * user.get_mana_damage()

	def is_negative(self):
		return True

class DevilPower(Buff):
	def __init__(self,):
		super(DevilPower, self).__init__(8, name='devilpow', damage_plus=3000000)
	def on_end(self, user, reply, room):
		reply(locale_manager.get('buffs.phrase_103'))
		user.remove_item('lepergold')
		user.remove_tag(DEVIL)
		user.death(reply, reason=locale_manager.get('buffs.phrase_104'))

class DevilInt(Buff):
	def __init__(self,):
		super(DevilInt, self).__init__(8, name='devilint', mana_damage_plus=3000000)
	def on_end(self, user, reply, room):
		reply(locale_manager.get('buffs.phrase_105'))
		user.remove_item('lepergold')
		user.remove_tag(DEVIL)
		user.death(reply, reason=locale_manager.get('buffs.phrase_106'))

class DevilMoney(Buff):
	def __init__(self,):
		super(DevilMoney, self).__init__(8, name='devilmon', mana_damage_plus=0)
	def on_end(self, user, reply, room):
		reply(locale_manager.get('buffs.phrase_107'))
		user.remove_item('lepergold')
		user.remove_tag(DEVIL)
		user.death(reply, reason=locale_manager.get('buffs.phrase_108'))

class DevilEntity(Buff):
	def __init__(self,):
		super(DevilEntity, self).__init__(8, name='devilent', damage_plus=3000000, mana_damage_plus=3000000)
	def on_end(self, user, reply, room):
		reply(locale_manager.get('buffs.phrase_109'))
		user.remove_item('lepergold')
		user.remove_tag(DEVIL)
		user.death(reply, reason=locale_manager.get('buffs.phrase_110'))

class EmperorDefence(Buff):
	def __init__(self):
		super(EmperorDefence, self).__init__(5, name='emperordef', defence=25)

class EmperorBurn(Buff):
	def __init__(self):
		super(EmperorBurn, self).__init__(3, name='emperorburn')
	def on_room(self, user, reply, room):
		self.time -= 1
		user.make_damage(10, 20, reply, death=True, name=locale_manager.get('buffs.phrase_111'))
		reply(locale_manager.get('buffs.phrase_112'))	

class DiabetBuff(Buff):
	def __init__(self):
		super(DiabetBuff, self).__init__(3, name='diabet')
	def on_room(self, user, reply, room):
		user.make_damage(10, 20, reply, death=True, name=locale_manager.get('buffs.phrase_113'))
		reply(locale_manager.get('buffs.phrase_114'))	

	def is_negative(self):
		return True

class ScrollBuff_armor(Buff):
	def __init__(self):
		super(ScrollBuff_armor, self).__init__(2, name='scrolldef', defence=1000)