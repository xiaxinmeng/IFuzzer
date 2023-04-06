# coding: utf-8
import logging

logging.basicConfig()
try:
    raise Exception(u'ą')
except Exception:
    logging.getLogger('general').exception(u'An error occurred')