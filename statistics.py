import botan
import config

tkn = None

if hasattr(config, 'BOTANIO_TOKEN'):
	tkn = config.BOTANIO_TOKEN

def track(uid, message, name='Message'):
	if tkn is not None:
		arg = message
		try:
			arg = {
				'text': message.text,
				'date': message.date.isoformat()
				#'from_user': message.from_user.__dict__
			}
		except:
			pass

		botan.track(tkn, uid, arg, name)

def get_link(uid):
	return botan.shorten_url('https://telegram.me/storebot?start=rog_bot', tkn, uid)
