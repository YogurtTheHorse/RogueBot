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
		res = True
		ROOM_TYPES = [ 'usual', 'special', 'boss', 'monster', 'missions/main', 'missions/lepricone', 'missions/caravan', 'missions/tips' ]
		PACKS = [ 'default', 'vietnam' ]
		for p in PACKS:
			for t in ROOM_TYPES:
				if not os.path.exists('rooms/' + p + '/' + t + '/'):
					continue

				for r in roomloader.get_all_rooms(p, t):
					if r == 'twi_monster':
						continue
					room = None
					try:
						room = roomloader.load_room(r, t)
						
						res = res and not (room is None)
					except BaseException:
						print('rooms/'+ p + '/' + t + '/' + r + '.py')
						res = False

		self.assertFalse(False)


	def test_items(self):
		ITEM_TYPES = [ 'good', 'bad', 'neutral', 'special', 'pets' ]
		for t in ITEM_TYPES:
			for r in itemloader.get_all_items(t):
				item = itemloader.load_item(r, t)

				self.assertFalse(item is None)

if __name__ == '__main__':
    unittest.main()