from localizations import locale_manager
from utils.buffs import VietnamBuff

name = locale_manager.get('rooms.vietnam.usual.trap.phrase_1')

def enter(user, reply):
	reply(
		locale_manager.get('rooms.vietnam.usual.trap.phrase_2')'Стальные челюсти захлопываются на твоих ногах. Чёрт! '
		locale_manager.get('rooms.vietnam.usual.trap.phrase_3'))

def get_actions(user):
	return [ locale_manager.get('rooms.vietnam.usual.trap.phrase_4')]

def action(user, reply, text):
	user.new_buff(VietnamBuff())
	user.leave(reply)