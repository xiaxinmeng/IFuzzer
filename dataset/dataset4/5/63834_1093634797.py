# Skip tests if _multiprocessing wasn't built.            
test.support.import_module('_multiprocessing')   
# Skip tests if sem_open implementation is broken.                        
test.support.import_module('multiprocessing.synchronize')
# import threading after _multiprocessing to raise a more revelant error  
# message: "No module named _multiprocessing". _multiprocessing is not compiled
# without thread support.
test.support.import_module('threading')