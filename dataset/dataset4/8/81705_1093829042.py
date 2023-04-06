# In 3.4, if no shell window is ever open, the underlying Tk widget is
# destroyed before .__del__ methods here are called.  The following
# is used to selectively ignore shutdown exceptions to avoid
# 'Exception ignored' messages.  See http://bugs.python.org/issue20167
APPLICATION_GONE = "application has been destroyed"