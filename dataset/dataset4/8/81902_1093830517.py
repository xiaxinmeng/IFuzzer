import logging
import sys
logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)

from smtpd import DebuggingServer as TestMailServer
import threading
from notifiers import get_notifier
import time
import itertools as it

mail_server = threading.Thread(target=TestMailServer, args=(("localhost", 2500), None))
mail_server.daemon = True
mail_server.start()

time.sleep(2)


for msg in it.repeat('copy', 100):
    print(msg)
    get_notifier('email').notify(from_='cherusk@localhost',
                                 to='root@localhost',
                                 message=msg,
                                 subject='TST',
                                 host='localhost',
                                 port=2500,
                                 tls=False,
                                 ssl=False,
                                 html=False,
                                 username="some",
                                 password='pw'
                                 )