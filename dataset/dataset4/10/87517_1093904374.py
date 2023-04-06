
#0  0x00002aaaaef63337 in raise () from /lib64/libc.so.6
#1  0x00002aaaaef64a28 in abort () from /lib64/libc.so.6
#2  0x00002aaaae726e18 in fatal_error (prefix=0x0, msg=0x2aaaae8091f0 "Cannot recover from stack overflow.", status=-1) at Python/pylifecycle.c:2187
#3  0x00002aaaae727603 in Py_FatalError (msg=0x9bf0 <Address 0x9bf0 out of bounds>) at Python/pylifecycle.c:2197
#4  0x00002aaaae6ede2b in _Py_CheckRecursiveCall (where=<optimized out>) at Python/ceval.c:489
#5  0x00002aaaae62b61d in _PyMethodDef_RawFastCallDict (method=0x2aaaaeae2740 <textiowrapper_methods+160>, self=0x2aaabb1d4d70, args=0x0, nargs=0, kwargs=0x0) at Objects/call.c:464
#6  0x00002aaaae62b6a9 in _PyCFunction_FastCallDict (func=0x2aaabeaa5690, args=0x6, nargs=0, kwargs=0x0) at Objects/call.c:586
#7  0x00002aaaae62c56c in _PyObject_CallFunctionVa (callable=0x9bf0, format=<optimized out>, va=<optimized out>, is_size_t=<optimized out>) at Objects/call.c:935
#8  0x00002aaaae62cc80 in callmethod (is_size_t=<optimized out>, va=<optimized out>, format=<optimized out>, callable=<optimized out>) at Objects/call.c:1031
#9  _PyObject_CallMethodId (obj=<optimized out>, name=<optimized out>, format=0x0) at Objects/call.c:1100
#10 0x00002aaaae724c51 in flush_std_files () at Python/pylifecycle.c:1083
#11 0x00002aaaae72704f in fatal_error (prefix=0x0, msg=<optimized out>, status=-1) at Python/pylifecycle.c:2175
#12 0x00002aaaae727603 in Py_FatalError (msg=0x9bf0 <Address 0x9bf0 out of bounds>) at Python/pylifecycle.c:2197
#13 0x00002aaaae6ede2b in _Py_CheckRecursiveCall (where=<optimized out>) at Python/ceval.c:489
#14 0x00002aaaae62ba3d in _PyObject_FastCallDict (callable=0x2aaabeab8790, args=<optimized out>, nargs=<optimized out>, kwargs=0x0) at Objects/call.c:120
#15 0x00002aaaae62c2f0 in object_vacall (callable=0x2aaabeab8790, vargs=0x7ffffff54d40) at Objects/call.c:1202
#16 0x00002aaaae62c3fd in PyObject_CallFunctionObjArgs (callable=0x9bf0) at Objects/call.c:1267
#17 0x00002aaaae6c1bf0 in PyObject_ClearWeakRefs (object=<optimized out>) at Objects/weakrefobject.c:872
#18 0x00002aaaae4b26f6 in instance_dealloc () from /home/LOCAL/avj/build/vc21__90601_pyedg_improvements/vc/lib64/libboost_python37.so.1.69.0
#19 0x00002aaaae67c3e0 in subtype_dealloc (self=0x2aaabeab9e40) at Objects/typeobject.c:1176
#20 0x00002aaaae4ba63f in life_support_call () from /home/LOCAL/avj/build/vc21__90601_pyedg_improvements/vc/lib64/libboost_python37.so.1.69.0
#21 0x00002aaaae62b9c4 in _PyObject_FastCallDict (callable=0x2aaabeab87b0, args=<optimized out>, nargs=<optimized out>, kwargs=0x0) at Objects/call.c:125
#22 0x00002aaaae62c2f0 in object_vacall (callable=0x2aaabeab87b0, vargs=0x7ffffff54fd0) at Objects/call.c:1202
#23 0x00002aaaae62c3fd in PyObject_CallFunctionObjArgs (callable=0x9bf0) at Objects/call.c:1267
#24 0x00002aaaae6c1bf0 in PyObject_ClearWeakRefs (object=<optimized out>) at Objects/weakrefobject.c:872
#25 0x00002aaaae4b26f6 in instance_dealloc () from /home/LOCAL/avj/build/vc21__90601_pyedg_improvements/vc/lib64/libboost_python37.so.1.69.0
#26 0x00002aaaae67c3e0 in subtype_dealloc (self=0x2aaabeab9e90) at Objects/typeobject.c:1176
#27 0x00002aaaae4ba63f in life_support_call () from /home/LOCAL/avj/build/vc21__90601_pyedg_improvements/vc/lib64/libboost_python37.so.1.69.0
#28 0x00002aaaae62b9c4 in _PyObject_FastCallDict (callable=0x2aaabeab87d0, args=<optimized out>, nargs=<optimized out>, kwargs=0x0) at Objects/call.c:125
#29 0x00002aaaae62c2f0 in object_vacall (callable=0x2aaabeab87d0, vargs=0x7ffffff55260) at Objects/call.c:1202
#30 0x00002aaaae62c3fd in PyObject_CallFunctionObjArgs (callable=0x9bf0) at Objects/call.c:1267
#31 0x00002aaaae6c1bf0 in PyObject_ClearWeakRefs (object=<optimized out>) at Objects/weakrefobject.c:872
#32 0x00002aaaae4b26f6 in instance_dealloc () from /home/LOCAL/avj/build/vc21__90601_pyedg_improvements/vc/lib64/libboost_python37.so.1.69.0
#33 0x00002aaaae67c3e0 in subtype_dealloc (self=0x2aaabeab9ee0) at Objects/typeobject.c:1176
#34 0x00002aaaae4ba63f in life_support_call () from /home/LOCAL/avj/build/vc21__90601_pyedg_improvements/vc/lib64/libboost_python37.so.1.69.0
