import imp
import os

def __fork():
  imp.acquire_lock()
  try:
    return _os_fork()
  finally:
    imp.release_lock()