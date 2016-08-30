import config

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import usermanager
import telegram
import logging
import os

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
					level=logging.INFO)

logger = logging.getLogger('rg')

def reply(c_id, bot, txt, buttons=None, photo=None):
	if buttons:
		custom_keyboard = [ [ x ] for x in buttons ]
		reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard, one_time_keyboard=True)
		bot.sendMessage(c_id, text=txt, reply_markup=reply_markup, parse_mode=telegram.ParseMode.MARKDOWN)
	else:
		bot.sendMessage(c_id,
						text=txt, 
						parse_mode=telegram.ParseMode.MARKDOWN)

	if photo:
		bot.sendPhoto(c_id, photo=open('images/{0}'.format(photo), 'rb'))

def start(bot, update):
	bot.sendMessage(update.message.chat_id, text='Теперь скажи мне свое имя.')
	usermanager.new_user(update.message.chat_id)

def setname(bot, update):
	txt = update.message.text.split()
	if len(txt) > 9:
		name = update.message.text[10:]
		usermanager.setname(update.message.chat_id, name)

		bot.sendMessage(update.message.chat_id, text='Ну хорошо')

def debug_print(bot, update):
	inf = usermanager.debug_info(update.message.chat_id)
	bot.sendMessage(update.message.chat_id, text=inf)

def room(bot, update):
	c_id = update.message.chat_id

	if str(c_id) in config.ADMINS_IDS:
		cmd, room_type, name = update.message.text.split()
		usermanager.open_room(c_id, lambda *a, **kw: reply(c_id, bot, *a, **kw), room_type, name)
	else:
		bot.sendMessage(update.message.chat_id, text='NO.')

def give(bot, update):
	if str(update.message.chat_id) in config.ADMINS_IDS:
		cmd, item_type, name = update.message.text.split()
		usermanager.give_item(update.message.chat_id, item_type, name)
	else:
		bot.sendMessage(update.message.chat_id, text='NO.')

def msg(bot, update):
	c_id = update.message.chat_id

	global msg, image, buttons
	msg = ''
	image = None
	buttons = None

	def rep(txt, btns=None, pht=None):
		global msg, image, buttons

		msg += '\n\n'
		msg += txt

		if btns:
			buttons = btns
		if pht:
			image = pht

	usermanager.message(c_id, rep, update.message.text)

	reply(c_id, bot, msg, buttons, image)

def error_callback(bot, update, error):
	error_msg = 'User "%s" had error "%s"' % (update.message.chat_id, error)
	logger.warn(error_msg)
	msg = 'Ошибка внутри сервера. Если это мешает играть, сообщите @yegorf1'
	bot.sendMessage(update.message.chat_id, text=msg)
	bot.sendMessage(update.message.chat_id, 
					text='```text\n{0}\n```'.format(error_msg),
					parse_mode=telegram.ParseMode.MARKDOWN)

if not os.path.isdir('users'):
	logger.info('Creating users directory')
	os.makedirs('users')

logger.info('Creating Updater...')
updater = Updater(config.TELEGRAM_TOKEN)

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('debug', debug_print))
updater.dispatcher.add_handler(CommandHandler('setname', setname))
updater.dispatcher.add_handler(CommandHandler('room', room))
updater.dispatcher.add_handler(CommandHandler('give', give))
updater.dispatcher.add_handler(MessageHandler(False, msg))
updater.dispatcher.add_error_handler(error_callback)

logger.info('Starting polling...')
updater.start_polling()
logger.info('Bot now officially started!')
updater.idle()
