from localizations import locale_manager
from constants import *
from utils.buffs import ScrollBuff_armor
import random

name = locale_manager.get('items.good.scroll_armor.phrase_1')

description = (
	locale_manager.get('items.good.scroll_armor.phrase_2')
)

price = 100

fightable = True
disposable = True

def fight_use(user, reply, room):
	if user.use_mana(50):
		reply(locale_manager.get('items.good.scroll_armor.phrase_3'))
		user.new_buff(ScrollBuff_armor())
	else:
		reply(locale_manager.get('items.good.scroll_armor.phrase_4'))
		user.add_item('good', 'scroll_armor')
	return 0
