length = int(os.environ.get('CONTENT_LENGTH', None))
"""Length fix for IIS 7.x to avoid hang up"""
length=length-2