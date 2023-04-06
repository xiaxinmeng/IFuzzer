appsLib =cdll.LoadLibrary(util.find_library('ApplicationServices'))
event = appsLib.CGEventCreate(None);
pt = appsLib.CGEventGetLocation(event);