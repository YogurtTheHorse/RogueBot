from collections import Counter
import items.itemloader as itemloader

def remove_item(self, code_name):
	ind = -1
	for i in range(len(self.items)):
		if self.items[i][1] == code_name:
			ind = i
			break

	if ind >= 0:
		del self.items[ind]

def remove_items_with_tag(self, tag):
	items = self.get_items()
	active_items = self.get_active_items()

	new_items = [ (i.buff, i.code_name) for i in items if tag not in i.tags ]
	new_active_items = [ (i.buff, i.code_name) for i in active_items if tag not in i.tags ]

	self.items = new_items
	self.active_items = new_items

def deactivate_item_by_name(self, name):
	ind = -1
	active_items = self.get_active_items()
	for i in range(len(self.active_items)):
		if active_items[i].name == name:
			ind = i
			break

	if ind >= 0:
		del self.active_items[ind]

		return True
	return False

def remove_item_by_name(self, name):
	ind = -1
	items = self.get_items()
	for i in range(len(self.items)):
		if items[i].name == name:
			ind = i
			break

	if ind >= 0 and items[ind] and not items[ind].iscursed:
		del self.items[ind]

		return True
	return False

def get_item_by_name(self, name):
	items = self.get_items()
	
	for i in items:
		if i.name == name:
			return i

	return None	

def get_items(self):
	def load_item(i):
		if len(i) >= 3:
			return itemloader.load_item(i[1], i[0], i[2], self)
		else:
			return itemloader.load_item(i[1], i[0], { }, self)

	return [ i for i in [ load_item(i) for i in self.items ] if i is not None ]

def get_active_items(self):
	return self.get_items()

def get_counted_items(self):
	items = self.get_active_items()
	counter = Counter(items)

	return counter.most_common()

def get_active_slots_len(self):
	return 10 + self.rooms_count // 15

def has_item(self, code_name):
	for i in self.items:
		if i[1] == code_name:
			return True

	return False

def add_item(self, buff, name, context={}):
	self.items.append( (buff, name, context) )
