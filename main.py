from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

def start(bot, update):
    bot.sendMessage(update.message.chat_id, text='Hi!')

def echo(bot, update):
    bot.sendMessage(update.message.chat_id, text=update.message.text)

def hello(bot, update):
    bot.sendMessage(update.message.chat_id,
                    text='Hello {0}'.format(update.message.from_user.first_name))

logger.info('Creating Updater...')
updater = Updater('253526115:AAGBxSDWqJYxwFAZG8rpn1LDwtG1StIBWsk')

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('hello', hello))

updater.dispatcher.add_handler(MessageHandler(False, echo))

logger.info('Starting polling...')
updater.start_polling()
logger.info('Bot now officially started!')
updater.idle()
