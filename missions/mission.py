class Mission(object):
	def __init__(self, name, room_name, path_length=10):
		super(Mission, self).__init__()
		self.name = name
		self.room_name = room_name
		self.path_length = path_length

	def is_ready(self):
		return self.path_length <= 0

	def room_opened(self):
		self.path_length -= 1

	def get_room_type(self):
		return 'missions/{0}'.format(self.name)

	def get_room_name(self):
		return self.room_name