#-*- coding: UTF-8 -*-
from rooms import roomloader
from items import itemloader
import yaml
import os
import re

#ROOM_TYPES = [ 'usual', 'special', 'boss', 'monster', 'missions/main', 'missions/lepricone', 'missions/caravan', 'missions/tips' ]
ROOM_TYPES = [ 'monster/easy', 'monster/medium', 'monster/hard' ]
PACKS = [ 'default', 'vietnam' ]
ITEM_TYPES = [ 'good', 'bad', 'neutral', 'special', 'pets', 'loot', 'pets', 'story' ]

full_yaml = { }

f_letter_re = r'[А-Яа-я0-9\. \!\?\—\*с_ёЁ»—«#\(]|-|:|\{|\}|\\'
text_re = '(' + f_letter_re +  ')(' + f_letter_re + r'|[A-Za-z\,\)\№])+'
str_re = '\'' + text_re + '\''
big_str_re = '(\'' + text_re + r'\'(\n\t| |\t|\n)*){2,}'

def work_room(path, pack, tp, code_name):
	print(path)

	yaml_vars = { }

	new_data = 'from localizations import locale_manager\n'
	with open(path, 'r') as myfile:
		old_data = myfile.read()

	global ph_num
	ph_num = 0

	def str_repl(mathcobj):
		global ph_num
		ph_num += 1
		k = 'phrase_{0}'.format(ph_num)

		yaml_vars[k] = eval('(' + mathcobj.group(0) + ')')

		return 'locale_manager.get(\'rooms.{0}.{1}.{2}.{3}\')'.format(pack, tp.replace('/', '_'), code_name, k)

	new_data += re.sub(big_str_re, str_repl, old_data, re.MULTILINE)
	new_data = re.sub(str_re, str_repl, new_data)

	with open(path, 'w') as new_file:
		new_file.write(new_data)

	if pack not in full_yaml:
		full_yaml[pack] = { }

	if tp.replace('/', '_') not in full_yaml[pack]:
		full_yaml[pack][tp.replace('/', '_')] = { }

	full_yaml[pack][tp.replace('/', '_')][code_name] = yaml_vars

def work_item(path, tp, code_name):
	print(path)

	yaml_vars = { }

	new_data = 'from localizations import locale_manager\n'
	with open(path, 'r') as myfile:
		old_data = myfile.read()

	global ph_num
	ph_num = 0

	def str_repl(mathcobj):
		global ph_num
		ph_num += 1
		k = 'phrase_{0}'.format(ph_num)

		yaml_vars[k] = eval('(' + mathcobj.group(0) + ')')

		return 'locale_manager.get(\'items.{0}.{1}.{2}\')'.format(tp, code_name, k)

	new_data += re.sub(big_str_re, str_repl, old_data, re.MULTILINE)
	new_data = re.sub(str_re, str_repl, new_data)

	with open(path, 'w') as new_file:
		new_file.write(new_data)

	if tp not in full_yaml:
		full_yaml[tp] = { }

	full_yaml[tp][code_name] = yaml_vars


def rooms():
	for p in PACKS:
		for t in ROOM_TYPES:
			fldr_pth = 'rooms/' + p + '/' + t + '/'

			if not os.path.exists(fldr_pth):
				continue

			rooms =  [ f for f in os.listdir(fldr_pth) if f.endswith('.py') ]

			for r in rooms:
				if r == 'helloween_quest.py':
					continue 

				full_path = fldr_pth + r

				work_room(full_path, p, t, r[:-3])

def items():
	for t in ITEM_TYPES:
		for i in itemloader.get_all_items(t):
			pth = 'items/{0}/{1}.py'.format(t, i)
			work_item(pth, t, i)

rooms()
with open('localizations/tmp.yaml', 'w') as f:
	yaml.dump({'ru-RU': {'rooms': full_yaml} }, f, default_flow_style=False, allow_unicode=True, width=1000)
