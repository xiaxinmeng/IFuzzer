import time
DATE_FORMAT = '%d/%b/%Y %H:%M:%S%z %Z'
print(time.strftime(DATE_FORMAT))
print(time.strftime(DATE_FORMAT,time.localtime()))