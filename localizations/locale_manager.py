import yaml
import config
import logging

logger = logging.getLogger('rg')
loaded_locales = { }

global language
language = 'ru_RU' if ('LANG' not in config.__dict__) else config.LANG

def get_language():
	global language
	return language

def set_language(lang):
	global language
	language = lang

def get_locale(language=None):
	if language is None:
		language = get_language()

	if language not in loaded_locales:
		loaded_locales[language] = dict()
		try:
			with open('localizations/{0}.yml'.format(language), encoding='utf-8') as lang_file:
				loaded_locales[language] = yaml.load(lang_file)[language]
		except BaseException as e:
			logger.warn('Error loading "{0}" locale: {1}'.format(language, e))

	return loaded_locales[language]

def get(code_name, language=None):
	locale = get_locale(language)
	keys = code_name.split('.')

	translation = _get(keys, locale)

	if translation is None:
		return 'Missing translation: {}, language: {}'.format(code_name, language)

	return translation

def _get(keys, locale):
	head, *tail = keys

	if head in locale:
		new_locale = locale[head]
		if not tail:
			if isinstance(new_locale, str):
				return new_locale
		else:
			if isinstance(new_locale, object):
				return _get(tail, new_locale)

	return None
