class rewrite_list_eq(list) :
    def __eq__(self,other) :
        str(other)
        return NotImplemented

class poc() :
    def __eq__(self,other) :
        list1.clear()
        return NotImplemented

list1 = rewrite_list_eq([ poc() ])
list1.remove(list1)   #  list_count() -> PyObject_RichCompareBool()