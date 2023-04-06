import Carbon.CoreFoundation as CF
from appscript import LaunchServices

path = 'TextEdit.app'

fURL = LaunchServices.LSFindApplicationForInfo ('????', None, 
path)[1]