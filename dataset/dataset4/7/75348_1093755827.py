# create a circular reference with a malicious __del__().
class A:
    def __del__(*args):
        del list1[0]
circ_ref_obj = A()
circ_ref_obj._self = circ_ref_obj

list1 = [None]
list2 = []
del circ_ref_obj
while len(list2) < 10000:
    list2.append(list1[:])