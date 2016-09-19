import logging
from daemonize import Daemonize
from main import main

pid = "/var/run/rogbot.pid"
logger = logging.getLogger("rb")
logger.setLevel(logging.DEBUG)
logger.propagate = False
fh = logging.FileHandler("rogbot.log", "w")
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)
keep_fds = [fh.stream.fileno()]


daemon = Daemonize(app="rogbot", pid=pid, action=main, keep_fds=keep_fds)
daemon.start()