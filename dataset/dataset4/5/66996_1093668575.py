from uuid import UUID
import ctypes
import ctypes.util

lib = ctypes.CDLL(ctypes.util.find_library('uuid'))
_ugts = lib.uuid_generate_time_safe

_buffer = ctypes.create_string_buffer(16)
retval = _ugts(_buffer)

# Remember, this is C!
is_safe = (retval == 0)