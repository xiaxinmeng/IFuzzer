from __future__ import print_function
import ctypes
import ctypes.util

lib_location = ctypes.util.find_library('gettextpo')
gpo = ctypes.cdll.LoadLibrary(lib_location)

gpo_message = gpo.po_message_create()
source = "foo"

print("calling po_message_set_msgid")
gpo.po_message_set_msgid(gpo_message, source.encode('utf-8'))

print("success")