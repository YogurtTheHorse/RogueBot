from mongothon.model import NotFoundException

from mongothon import Schema
from mongothon import create_model

var_schema = Schema({
		'name': {"type": str, "required": True},
		'value': {"type": object, "required": True }
	})

def get_model(db):
	Variables = create_model(var_schema, db['vars'])

	@Variables.class_method
	def get_value(cls, name, def_val=None):
		try:
			return cls.find_one({'name': name})['value']
		except:
			return def_val

	@Variables.class_method
	def set_value(cls, name, value):
		try:
			var = cls.find_one({'name': name})
			var.update({'value': value})
			var.save()
		except:
			var = Variables({'name': name, 'value': value})
			var.save()

	return Variables