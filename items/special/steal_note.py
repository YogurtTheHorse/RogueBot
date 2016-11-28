from localizations import locale_manager
import items.itemloader as itemloader

context = itemloader.get_context()

name = locale_manager.get('items.special.steal_note.phrase_1')
price = 1
description = locale_manager.get('items.special.steal_note.phrase_2')

usable = True

def on_use(user, reply):
	stealer = user.get_variable('stealer', 'none')

	thought = locale_manager.get('items.special.steal_note.phrase_3')
	if stealer != 'none':
		thought = locale_manager.get('items.special.steal_note.phrase_4').format(stealer)
	else:
		thought = locale_manager.get('items.special.steal_note.phrase_5').format(context['stealer'], context['item_name'])

	reply(locale_manager.get('items.special.steal_note.phrase_6'))
	reply(locale_manager.get('items.special.steal_note.phrase_7').format(thought))
