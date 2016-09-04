import yaml
import config
import logging

logger = logging.getLogger('rg')

def get_language():
	try:
		return config.LANG
	except:
		return 'ru-RU'

def get_locale(language=None):
	if language is None:
		language = get_language()

	locale = dict()

	try:
		with open('localizations/{0}.yml'.format(language), encoding='utf-8') as lang_file:
			locale = yaml.load(lang_file)[language]
	except BaseException as e:
		logger.warn('Error loading "{0}" locale: {1}'.format(language, e))

	return locale

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
