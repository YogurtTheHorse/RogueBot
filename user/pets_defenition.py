import logging
import usermanager
import items.itemloader as itemloader
logger = logging.getLogger('rg')

def new_pet(self, reply, pet):
	if self.pet:
		self.state = 'pet_confirm'
		name = self.pet[1]

		self.set_variable('new_pet', pet)
		reply('У тебя уже есть питомец по имени {0}. Взять другого?'.format(name), [ 'Да', 'Нет' ])
	else:
		self.state = 'pet_name'
		self.pet = pet
		reply('Класс! У тебя новый питомец!\nКак ты его назовешь?', [])

def on_pet(self, reply, text):
	if self.state == 'pet_confirm':
		if text == 'Да':
			name = self.pet[1]
			reply('Прощай, {0}'.format(name))
			reply('Как назовем нового?')
			self.pet = self.get_variable('new_pet')
			self.state = 'pet_name'
		else:
			reply('Видно не судьба')
			self.leave(reply)
	else:
		if '_' in text:
			reply('Это же _питомец_! Зачем тебе подчеркивания в его имени?')
		else:
			usr = usermanager.random_user()
			reply('Отличный выбор. Наверное.. Я свою дочь вообще назвал {0}. Нет у меня вкуса'.format(usr.name))
			self.pet = (self.pet, text)
			self.leave(reply)

def get_pet(self):
	if self.pet is None:
		return None

	pet = itemloader.load_item(self.pet[0], 'pets')
	pet.real_name = self.pet[1]

	return pet

def pet_gone(self):
	self.pet = None