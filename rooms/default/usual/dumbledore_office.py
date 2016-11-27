from localizations import locale_manager
name = locale_manager.get('rooms.default.usual.dumbledore_office.phrase_1')

def get_actions(user):
	return [locale_manager.get('rooms.default.usual.dumbledore_office.phrase_2')]

#Цитата из книги, описание кабинета директора Хогвартса. Пока как просто маленькая пасхалочка, потенциально может вылиться в мини-квест по тематики ГП.
def enter(user, reply):
    reply(locale_manager.get('rooms.default.usual.dumbledore_office.phrase_3') +
          locale_manager.get('rooms.default.usual.dumbledore_office.phrase_4') +
          locale_manager.get('rooms.default.usual.dumbledore_office.phrase_5') +
          locale_manager.get('rooms.default.usual.dumbledore_office.phrase_6') +
          locale_manager.get('rooms.default.usual.dumbledore_office.phrase_7') +
          locale_manager.get('rooms.default.usual.dumbledore_office.phrase_8')) 

def action(user, reply, text):
      user.leave(reply)