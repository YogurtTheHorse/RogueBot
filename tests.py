import os
import sys
import config
import unittest
from rooms import roomloader
from items import itemloader

sys.path.append(".") 

def foo(*v, **kw):
	pass

class Tests(unittest.TestCase):
	def test_config(self):
		self.assertTrue(hasattr(config, 'TELEGRAM_TOKEN') or (hasattr(config, 'VK_LOGIN') and hasattr(config, 'VK_PASS')))
		self.assertTrue(hasattr(config, 'ADMINS_IDS'))
		self.assertTrue(hasattr(config, 'MODERS_IDS'))
		#self.assertTrue(hasattr(config, 'USERS_PATH'))
		#self.assertTrue(hasattr(config, 'DATABASE_PATH'))

	def test_folders(self):
		self.assertTrue(os.path.isdir(config.USERS_PATH))
		self.assertTrue(os.path.isfile(config.DATABASE_PATH))

	def test_rooms(self):
		ROOM_TYPES = [ 'usual', 'special', 'boss', 'monster', 'story' ]
		for t in ROOM_TYPES:
			for r in roomloader.get_all_rooms(t):
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