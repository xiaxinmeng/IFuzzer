
def bug42562():
      pass

bug42562.__code__ = bug42562.__code__.replace(co_linetable=b'\x04\x80\xff\x80')
