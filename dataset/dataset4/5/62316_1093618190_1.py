# bugme2.py
import os

fd = os.open('/dev/tty', os.O_RDWR|os.O_NOCTTY)
os.fdopen(fd, 'w+', 1)
# end of bugme2.py