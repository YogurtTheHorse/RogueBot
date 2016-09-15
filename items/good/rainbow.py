from utils.buffs import RainbowBuff

name = "Психопаста «Радуга»"
price = 100
description = (
	'Самый надежный спутник психовоина:\n\n'

	' - Эффективно устраняет трещины сознания\n'
	' - Снимает зуд базальных ганглий\n'
	' - Отпускает без рецепта\n'
)

usable = True
disposable = True

def on_use(user, reply):
	reply('О, да.')
	user.new_buff(RainbowBuff())
