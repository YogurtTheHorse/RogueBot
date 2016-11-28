from localizations import locale_manager
name = locale_manager.get('items.story.gun.phrase_1')
description = (
	locale_manager.get('items.story.gun.phrase_2')
)

price = 300

fightable = True

strengthoff = True

def fight_use(user, reply, room):
	if user.has_item('bullet'):
		reply(locale_manager.get('items.story.gun.phrase_3'))

		user.remove_item('bullet')

		return 30
	else:
		reply(locale_manager.get('items.story.gun.phrase_4'))

		return 10