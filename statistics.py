import botan
import config

tkn = None

if hasattr(config, 'BOTANIO_TOKEN'):
	tkn = config.BOTANIO_TOKEN

def track(uid, message, name='Message'):
	if tkn is not None:
		botan.track(tkn, uid, message, name)

