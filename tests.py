import os
import sys
import unittest
from rooms import roomloader
from items import itemloader

sys.path.append(".") 

def foo(*v, **kw):
	pass

class Tests(unittest.TestCase):
	def test_rooms(self):
		ROOM_TYPES = [ 'usual', 'special', 'boss', 'monster', 'missions/main' ]
		for t in ROOM_TYPES:
			for r in roomloader.get_all_rooms('default', t):
				if r == 'twi_monster':
					continue

				room = roomloader.load_room(r, t)

				self.assertFalse(room is None)

	def test_items(self):
		ITEM_TYPES = [ 'good', 'bad', 'neutral', 'special', 'pets' ]
		for t in ITEM_TYPES:
			for r in itemloader.get_all_items(t):
				item = itemloader.load_item(r, t)

				self.assertFalse(item is None)

if __name__ == '__main__':
    unittest.main()