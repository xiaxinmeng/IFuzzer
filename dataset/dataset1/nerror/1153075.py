class X(object):

    class __metaclass__(type):
        def mro(self):
            return [self, dict, object]


x = X()
x['key'] = 'value'    # dict_ass_sub() called with a non-PyDictObject -> crash

 	  	 
