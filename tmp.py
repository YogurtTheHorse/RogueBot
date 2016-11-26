#-*- coding: UTF-8 -*-
from rooms import roomloader
import yaml
import os
import re

ROOM_TYPES = [ 'usual', 'special', 'boss', 'monster', 'missions/main', 'missions/lepricone', 'missions/caravan', 'missions/tips' ]
PACKS = [ 'default', 'vietnam' ]

full_yaml = { }
str_re = r'\'[А-Яа-я]([А-Яа-я0-9,\. \!\?\(\)\—\*с_\-]|\\n)+\''
big_str_re = r'(\'[А-Яа-я]([А-Яа-яA-Za-z0-9,\. \!\?\(\)\—\*с_\-]|\\n)+\'(\n\t| |\t)*)+'

global n
n = 0

def work(path, pack, tp, code_name):
	print(path)

	yaml_vars = { }

	new_data = 'from localizations import locale_manager\n'
	with open(path, 'r') as myfile:
		old_data = myfile.read()

	global ph_num
	ph_num = 0

	def str_repl(mathcobj):
		n+=1
		global ph_num, n
		ph_num += 1
		k = 'phrase_{0}'.format(ph_num)

		yaml_vars[k] = eval('(' + mathcobj.group(0) + ')')

		return 'locale_manager.get(\'rooms.{0}.{1}.{2}.{3}\')'.format(pack, tp.replace('/', '_'), code_name, k)

	new_data = re.sub(big_str_re, str_repl, old_data, re.MULTILINE)
	new_data = re.sub(str_re, str_repl, new_data)

	with open(path+'n', 'w') as new_file:
		new_file.write(new_data)
		print(path+'n')

	if pack not in full_yaml:
		full_yaml[pack] = { }

	if tp.replace('/', '_') not in full_yaml[pack]:
		full_yaml[pack][tp.replace('/', '_')] = { }

	full_yaml[pack][tp.replace('/', '_')][code_name] = yaml_vars

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

			work(full_path, p, t, r[:-3])

print(n)

with open('localizations/tmp.yaml', 'w') as f:
	yaml.dump({'rooms': full_yaml}, f, default_flow_style=False, allow_unicode=True, width=1000)
