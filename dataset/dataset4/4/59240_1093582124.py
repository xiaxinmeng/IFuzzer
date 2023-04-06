b = array.array('u', "hello world")
s = CFStringCreateMutableWithExternalCharactersNoCopy(                      
        None, b, len(b), len(b), kCFAllocatorNull)