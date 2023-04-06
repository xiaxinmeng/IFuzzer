sys.path.append(unicode_dir)
imp.find_module(u"VaultsSearch") # fails
imp.find_module("VaultsSearch") # fails
sys.path.remove(unicode_dir)