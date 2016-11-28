from localizations import locale_manager
from utils.buffs import Buff

name = locale_manager.get('items.good.gold_sand.phrase_1')
price = 700
description = (
	locale_manager.get('items.good.gold_sand.phrase_2')
)

usable = True
disposable = True

def on_use(user, reply):
	reply(locale_manager.get('items.good.gold_sand.phrase_3'))

	has_gold_buff = False

	for b in user.buffs:
		if b.get_name() == 'gold':
			has_gold_buff = True
			break
	
	gold_bonus = 2
	if has_gold_buff:
		gold_bonus = 0
		reply(locale_manager.get('items.good.gold_sand.phrase_4'))

	bf = Buff(10, name='gold', gold_bonus=gold_bonus)

	user.new_buff(bf)
