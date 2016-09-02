import json
import config
import logging

logger = logging.getLogger('rg')

def get_language():
	try:
		return config.LANG
	except:
		return 'ru'

def get_locale(language=None):
	if language is None:
		language = get_language()

	locale = dict()

	try:
		with open('localizations/{0}.json'.format(language), encoding='utf-8') as lang_file:
			locale = json.load(lang_file)
	except BaseException as e:
		logger.warn('Error loading "{0}" locale: {1}'.format(language, e))

	return locale


def get(code_name, language=None):
	locale = get_locale(language)

	if code_name in locale:		
		return locale[code_name]
	else:
		if 'parent' in locale:
			return get(code_name, locale['parent'])

		return "NOT_IN_LOCALE"