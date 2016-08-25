import os
import vk_api
import config
import logging
import requests
import usermanager

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
					level=logging.INFO)

logger = logging.getLogger('rg')

vk = None
vk_id = -1

LONGPOLL_URL = 'https://{0}?act=a_check&key={1}&ts={2}&wait=25&mode=0'

def main():
	global vk
	vk_session = vk_api.VkApi(config.VK_LOGIN, config.VK_PASS)

	try:
		vk_session.authorization()
	except vk_api.AuthorizationError as error_msg:
		print(error_msg)
		return

	vk = vk_session.get_api()
	vk_id = vk.users.get()[0]['id']

	if not os.path.isdir('users'):
		logger.info('Creating users directory')
		os.makedirs('users')

	logger.info('Bot now officially started!')

	checkMessages()

def checkMessages():
	longPoll = vk.messages.getLongPollServer()

	while True:
		events = requests.get(LONGPOLL_URL.format(longPoll['server'], longPoll['key'], longPoll['ts'])).json()
		try:
			for ev in events['updates']:
				if ev[0] == 4 and ev[2] & 2 == 0:
					new_message(ev)
		except BaseException as e:
			logger.error('Error: ' + str(e))

		longPoll['ts'] = events['ts']

def reply(id, txt, buttons=None, photo=None):
	vk.messages.send(peer_id=id, message=txt)

	if buttons:
		msg = 'Возможные действия:\n\n'
		for b in buttons:
			msg += b + '\n'
		vk.messages.send(peer_id=id, message=msg)

	if photo:
		vk.messages.send(peer_id=id, message='Картинка: ' + photo)

def new_message(event):
	text = event[6]
	c_id = event[3]
	uid = 'vk' + str(c_id)

	if text == '/start':
		reply(c_id, 'Теперь скажи мне свое имя')
		usermanager.new_user(uid)
	else:
		usermanager.message(uid, lambda *a, **kw: reply(c_id, *a, **kw), event[6])


if __name__ == '__main__':
	logger.info('Starting...')
	main()