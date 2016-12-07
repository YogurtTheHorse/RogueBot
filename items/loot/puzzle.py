from localizations import locale_manager
import random

name = locale_manager.get('items.loot.puzzle.phrase_1')

description = locale_manager.get('items.loot.puzzle.phrase_2')

price = 150

usable = True
iscursed = True

def on_use(user, reply):
	reply(locale_manager.get('items.loot.puzzle.phrase_3'))

def on_room(user, reply, room):
	say = [ 
			locale_manager.get('items.loot.puzzle.phrase_25'),
			locale_manager.get('items.loot.puzzle.phrase_26'),
			locale_manager.get('items.loot.puzzle.phrase_27'),
			locale_manager.get('items.loot.puzzle.phrase_4'),
			locale_manager.get('items.loot.puzzle.phrase_5'),
			locale_manager.get('items.loot.puzzle.phrase_6'),
			locale_manager.get('items.loot.puzzle.phrase_7'),
			locale_manager.get('items.loot.puzzle.phrase_28'),
			locale_manager.get('items.loot.puzzle.phrase_8'),
			locale_manager.get('items.loot.puzzle.phrase_9'),
			locale_manager.get('items.loot.puzzle.phrase_10'),
			locale_manager.get('items.loot.puzzle.phrase_11'),
			locale_manager.get('items.loot.puzzle.phrase_29'),
			locale_manager.get('items.loot.puzzle.phrase_12'),
			locale_manager.get('items.loot.puzzle.phrase_30'),
			locale_manager.get('items.loot.puzzle.phrase_13'),
			locale_manager.get('items.loot.puzzle.phrase_14'),
			locale_manager.get('items.loot.puzzle.phrase_15'),
			locale_manager.get('items.loot.puzzle.phrase_16'),
			locale_manager.get('items.loot.puzzle.phrase_17'),
			locale_manager.get('items.loot.puzzle.phrase_18'),
			locale_manager.get('items.loot.puzzle.phrase_19'),
			locale_manager.get('items.loot.puzzle.phrase_20'),
			locale_manager.get('items.loot.puzzle.phrase_21'),
			locale_manager.get('items.loot.puzzle.phrase_22'),
			locale_manager.get('items.loot.puzzle.phrase_23'),
			locale_manager.get('items.loot.puzzle.phrase_24')
		]
	reply(random.choice(say))