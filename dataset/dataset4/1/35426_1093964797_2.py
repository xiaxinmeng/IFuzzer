sys.path.append(ascii_dir)
imp.find_module(u"VaultsSearch") # succeeds
imp.find_module("VaultsSearch") # succeeds
sys.path.remove(ascii_dir)