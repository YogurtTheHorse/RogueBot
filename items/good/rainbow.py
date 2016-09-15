import random
from utils.buffs import RainbowBuff
from utils.buffs import NegativeRainbowBuff

name = "Психопаста «Радуга»"
price = 100
description = (
	'Самый надежный спутник психовоина:\n\n'

	' — Эффективно устраняет трещины сознания\n'
	' — Снимает зуд базальных ганглий\n'
	' — Отпускает без рецепта\n'
)

usable = True
disposable = True

def on_use(user, reply):
	rainbows_count = 0
	for b in user.buffs:
		if isinstance(b, RainbowBuff):
			rainbows_count += 1

	p = 0.9 ** (rainbows_count - 1)
	if random.random() > p:
		reply('Дозировать.. Дозировать нужно, голубчик.')
		# Turn off positive effect
		for b in user.buffs:
			if isinstance(b, RainbowBuff):
				b.time = -1

		user.new_buff(NegativeRainbowBuff())
	else:
		reply('_О-даа_.')
		user.new_buff(RainbowBuff())
