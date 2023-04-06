from ctypes import cdll
dll = cdll.LoadLibrary('libX11.so.6')
d = dll.XOpenDisplay(None)
root = dll.XDefaultRootWindow(d)
dll.XWarpPointer(d,None,root,0,0,0,0,20,39)
dll.XCloseDisplay(d)
dll.XCloseDisplay(d) #2nd call, should not be called, is not needed. Causes seg fault.