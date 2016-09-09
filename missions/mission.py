class Mission(object):
	def __init__(self, name, path_length=10):
		super(Mission, self).__init__()
		self.name = name
		self.path_length = path_length
		