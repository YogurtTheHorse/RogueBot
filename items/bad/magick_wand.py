from localizations import locale_manager
name = locale_manager.get('items.bad.magick_wand.phrase_1')
description = (
	locale_manager.get('items.bad.magick_wand.phrase_2')
)

price = 100

fightable = True
disposable = True
def fight_use(user, reply, room):
	reply(locale_manager.get('items.bad.magick_wand.phrase_3'))
	user.death(reply, reason=locale_manager.get('items.bad.magick_wand.phrase_4'))

	return 0