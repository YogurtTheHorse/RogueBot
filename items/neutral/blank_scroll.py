from localizations import locale_manager

name = locale_manager.get('items.neutral.blank_scroll.phrase_3')

description = (
	locale_manager.get('items.neutral.blank_scroll.phrase_1'))

mp_cost = 50

price = 1000

usable = True
disposable = True


def on_use(user, reply):

	if user.has_item('tooth_basilisk'):

		if user.mp >= mp_cost:

			reply(
				locale_manager.get('items.neutral.blank_scroll.phrase_2'))

			user.remove_item('tooth_basilisk')
			user.mp -= mp_cost
			user.add_item('special', 'magic_scroll')

		else:
			reply(locale_manager.get('items.neutral.blank_scroll.phrase_4'))
			user.remove_item('tooth_basilisk')
			user.mp = 0

	else:
		reply(locale_manager.get('items.neutral.blank_scroll.phrase_5'))

