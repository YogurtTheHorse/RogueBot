from localizations import locale_manager

def open_other(self, reply):
	self.state = 'other'
	reply(
		locale_manager.get('other.message'),
		[
			locale_manager.get('other.ru'),
			locale_manager.get('other.en'),
			locale_manager.get('other.back')
		]
	)


def other(self, reply, text):
	if text == locale_manager.get('other.ru'):
		self.lang = 'ru-RU'
		locale_manager.set_language('ru-RU')
		self.open_other(reply)
	elif text == locale_manager.get('other.en'):
		self.lang = 'en'
		locale_manager.set_language('en')
		self.open_other(reply)
	else:
		self.open_corridor(reply)

