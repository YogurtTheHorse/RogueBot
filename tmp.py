#-*- coding: UTF-8 -*-
from rooms import roomloader
import yaml
import os
import re

ROOM_TYPES = [ 'usual', 'special', 'boss', 'monster', 'missions/main', 'missions/lepricone', 'missions/caravan', 'missions/tips' ]
PACKS = [ 'default', 'vietnam' ]

full_yaml = { }
str_re = r'\'([А-Яа-я\—Cc\{\}]|\»|\—|\«)([А-Яа-я0-9,\. \!\?\(\)\—\*с_]|\\n|-|»|—|«|:|\{|\}|ё)+\''
big_str_re = r'(\'([А-Яа-я\—Cc\{\}]|\»|\—|\«| )([А-Яа-я0-9,\. \!\?\(\)\—\*с_]|\\n|-|»|—|«|:|\{|\}|ё|\#)+\'(\n\t| |\t)*){2,}'

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


"""
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
"""
www = [ ('rooms/default/usual/orc_shop.py', 'default', 'usual', 'orc_shop' ), ('rooms/default/usual/vladislav.py', 'default', 'usual', 'vladislav' ), ('rooms/default/usual/watches.py', 'default', 'usual', 'watches' ), ('rooms/default/usual/clairvoyance.py', 'default', 'usual', 'clairvoyance' ), ('rooms/default/usual/chest.py', 'default', 'usual', 'chest' ), ('rooms/default/usual/spanish_girl.py', 'default', 'usual', 'spanish_girl' ), ('rooms/default/usual/fog_door.py', 'default', 'usual', 'fog_door' ), ('rooms/default/usual/comissar.py', 'default', 'usual', 'comissar' ), ('rooms/default/usual/water.py', 'default', 'usual', 'water' ), ('rooms/default/usual/musclelot.py', 'default', 'usual', 'musclelot' ), ('rooms/default/usual/river.py', 'default', 'usual', 'river' ), ('rooms/default/usual/lucifer_bank.py', 'default', 'usual', 'lucifer_bank' ), ('rooms/default/usual/roulette.py', 'default', 'usual', 'roulette' ), ('rooms/default/special/kodzima.py', 'default', 'special', 'kodzima' ), ('rooms/default/special/yegorf1.py', 'default', 'special', 'yegorf1' ), ('rooms/default/special/icecream.py', 'default', 'special', 'icecream' ), ('rooms/default/special/gabe.py', 'default', 'special', 'gabe' ), ('rooms/default/special/kiba.py', 'default', 'special', 'kiba' ), ('rooms/default/special/bill_gates.py', 'default', 'special', 'bill_gates' ), ('rooms/default/special/bill_cypher.py', 'default', 'special', 'bill_cypher' ), ('rooms/default/special/helloween_quest.py', 'default', 'special', 'helloween_quest' ), ('rooms/default/missions/caravan/caravan.py', 'default', 'missions/caravan', 'caravan' ), ('rooms/default/missions/caravan/first.py', 'default', 'missions/caravan', 'first' ), ('rooms/vietnam/usual/river.py', 'vietnam', 'usual', 'river' ), ('rooms/vietnam/special/kodzima.py', 'vietnam', 'special', 'kodzima' ), ('rooms/vietnam/special/yegorf1.py', 'vietnam', 'special', 'yegorf1' ), ('rooms/vietnam/special/icecream.py', 'vietnam', 'special', 'icecream' ), ('rooms/vietnam/special/gabe.py', 'vietnam', 'special', 'gabe' ), ('rooms/vietnam/special/kiba.py', 'vietnam', 'special', 'kiba' ), ('rooms/vietnam/special/bill_gates.py', 'vietnam', 'special', 'bill_gates' ), ('rooms/vietnam/special/bill_cypher.py', 'vietnam', 'special', 'bill_cypher' ), ('rooms/vietnam/missions/caravan/caravan.py', 'vietnam', 'missions/caravan', 'caravan' ), ('rooms/vietnam/missions/caravan/first.py', 'vietnam', 'missions/caravan', 'first' ) ]

for pth, p, t, c in www:
	work_room(pth, p, t, c)

with open('localizations/tmp.yaml', 'w') as f:
	yaml.dump({'rooms': full_yaml}, f, default_flow_style=False, allow_unicode=True, width=1000)
