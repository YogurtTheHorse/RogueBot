import botan
import config

tkn = None

if hasattr(config, 'BOTANIO_TOKEN'):
	tkn = config.BOTANIO_TOKEN

def track(uid, message, name='Message'):
	if tkn is not None:
		botan.track(tkn, uid, message, name)

def get_link(uid):
	return botan.shorten_url('https://telegram.me/storebot?start=rog_bot', tkn, uid)
