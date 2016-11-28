from localizations import locale_manager
import random
from utils.buffs import RainbowBuff
from utils.buffs import NegativeRainbowBuff

name = "Психопаста «Радуга»"
price = 100
description = (
	locale_manager.get('items.good.rainbow.phrase_1'))

usable = True
disposable = True

def on_use(user, reply):
	rainbows_count = 0
	for b in user.buffs:
		if isinstance(b, RainbowBuff):
			rainbows_count += 1

	p = 0.9 ** (rainbows_count - 1)
	if random.random() > p:
		reply(locale_manager.get('items.good.rainbow.phrase_2'))
		# Turn off positive effect
		for b in user.buffs:
			if isinstance(b, RainbowBuff):
				b.time = -1

		user.new_buff(NegativeRainbowBuff())
	else:
		reply(locale_manager.get('items.good.rainbow.phrase_3'))
		user.new_buff(RainbowBuff())
