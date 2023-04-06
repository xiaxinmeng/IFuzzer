# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os, errno
name = "ƒőő"
try:
    os.mkdir(name)
except OSError as err:
    if err.errno != errno.EEXIST:
        raise
os.statvfs(name)