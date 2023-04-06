class rewrite_list_eq(list) :
    def __eq__(self,other) :
        str(other)   #  <== that will call the object recall function tp_repr and call it ..
        return NotImplemented

class poc() :
    def __eq__(self,other) :
        list1.clear()
        return NotImplemented

list1 = [ poc() ]
list1.index(list1)   #  list_index_impl() -> PyObject_RichCompareBool()