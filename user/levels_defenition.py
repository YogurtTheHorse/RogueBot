def prepare_boss(self):
	next_level = self.get_next_level(True)

	if next_level not in self.levels and next_level is not None:
		self.levels.append(next_level)

def get_prev_level(self):
	if self.level == 'medium':
		return 'easy'
	elif self.level == 'hard':
		return 'medium'
	else:
		return None

def get_next_level(self, force=False):
	res = None
	if self.level == 'easy':
		res = 'medium'
	elif self.level == 'medium':
		res = 'hard'

	if res is not None and (res in self.levels or force):
		return res
	else:
		return None
