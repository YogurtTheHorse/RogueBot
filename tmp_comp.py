import yaml

ru = 'ru-RU'
en = 'en'

ru_file = 'localizations/{0}.yml'.format(ru)
en_file = 'localizations/{0}.yml'.format(en)

ru_dict = dict()
en_dict = dict()

def work(d, obj, depth=''):
	if isinstance(obj, dict):
		for k, v in obj.items():
			work(d, v, depth + '.' + k)
	else:
		d[depth[1:]] = obj
		#print('{0}: {1}'.format(depth[1:], repr(obj)))

with open(ru_file, encoding='utf-8') as lang_file:
	loaded_lang = yaml.load(lang_file)[ru]
	work(ru_dict, loaded_lang)

with open(en_file, encoding='utf-8') as lang_file:
	loaded_lang = yaml.load(lang_file)[en]
	work(en_dict, loaded_lang)

for k in ru_dict.keys():
	s = '{0}\n{1}\t{2}'
	r = repr(ru_dict[k])
	if k in en_dict:
		e = repr(en_dict[k])
	else:
		e = 'None'

	print(s.format(k, r, e))
