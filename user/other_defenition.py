from localizations import locale_manager

def open_other(self, reply):
	self.state = 'other'
	reply(
		locale_manager.get('other.message', self.lang),
		[
			locale_manager.get('other.ru', self.lang),
			locale_manager.get('other.en', self.lang),
			locale_manager.get('other.back', self.lang)
		]
	)


def other(self, reply, text):
	if text == locale_manager.get('other.ru', self.lang):
		self.lang = 'ru-RU'
		locale_manager.set_language('ru-RU')
		self.open_other(reply)
	elif text == locale_manager.get('other.en', self.lang):
		self.lang = 'en'
		locale_manager.set_language('en')
		self.open_other(reply)
	else:
		self.open_corridor(reply)

