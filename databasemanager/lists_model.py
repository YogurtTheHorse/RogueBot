from mongothon.model import NotFoundException

from mongothon import Schema
from mongothon import create_model

list_schema = Schema({
		'name': {"type": str, "required": True},
		'value': {"type": list, "required": True }
	})

def get_model(db):
	Lists = create_model(list_schema, db['vars'])

	@Lists.class_method
	def get_list(cls, name):
		try:
			return cls.find_one({'name': name})['value']
		except:
			return [ ]

	@Lists.class_method
	def set_list(cls, name, value):
		try:
			var = cls.find_one({'name': name})
			var.update({'value': value})
			var.save()
		except:
			var = Lists({'name': name, 'value': value})
			var.save()

	@Lists.class_method
	def clear_list(cls, name):
		cls.set_list(name, [ ])

	@Lists.class_method
	def remove_from_list(cls, name, val):
		lst = cls.get_list(cls, name)
		lst.remove(val)
		cls.set_list(name, lst)

	@Lists.class_method
	def add_to_list(cls, name, val, force=True):
		lst = cls.get_list(cls, name)
		
		if force or val not in lst:
			lst.append(val)
			cls.set_list(name, lst)

	return Lists