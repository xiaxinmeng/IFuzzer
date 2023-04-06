import os

def isrealfile(file):
    """
    Test if file is on the os filesystem
    """
    
    if not hasattr(file, 'fileno'): return False