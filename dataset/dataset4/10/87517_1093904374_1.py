
python/cpython#51607 0x00002aaaae4b26f6 in instance_dealloc () from /home/LOCAL/avj/build/vc21__90601_pyedg_improvements/vc/lib64/libboost_python37.so.1.69.0
python/cpython#51608 0x00002aaaae67c3e0 in subtype_dealloc (self=0x2aaabeaefdf0) at Objects/typeobject.c:1176
python/cpython#51609 0x00002aaaae6f2f46 in _PyEval_EvalFrameDefault (f=0x2aaabce48b30, throwflag=39920) at Python/ceval.c:1098
python/cpython#51610 0x00002aaaae62a959 in function_code_fastcall (co=<optimized out>, args=0x7fffffffd088, nargs=1, globals=<optimized out>) at Objects/call.c:283
python/cpython#51611 0x00002aaaae62ae44 in _PyFunction_FastCallDict (func=0x2aaabda07950, args=0x7fffffffd080, nargs=1, kwargs=0x0) at Objects/call.c:322
python/cpython#51612 0x00002aaaae62bbea in _PyObject_Call_Prepend (callable=0x2aaabda07950, obj=0x2aaabea92590, args=0x2aaabb193050, kwargs=0x0) at Objects/call.c:908
python/cpython#51613 0x00002aaaae62b9c4 in _PyObject_FastCallDict (callable=0x2aaabb253a50, args=<optimized out>, nargs=<optimized out>, kwargs=0x0) at Objects/call.c:125
python/cpython#51614 0x00002aaaae62c677 in _PyObject_CallFunctionVa (callable=0x2aaabb253a50, format=<optimized out>, va=<optimized out>, is_size_t=<optimized out>) at Objects/call.c:956
python/cpython#51615 0x00002aaaae62c93a in PyEval_CallFunction (callable=0x9bf0, format=0x9bf0 <Address 0x9bf0 out of bounds>, format@entry=0x2aaaaaedba92 "()") at Objects/call.c:998
python/cpython#51616 0x00002aaaaae6ae16 in boost::python::call<boost::python::api::object> (callable=<optimized out>) at /home/BUILD64/lib/boost-1.69.0-py37/include/boost/python/call.hpp:56
python/cpython#51617 0x00002aaaaae6ae5a in boost::python::api::object_operators<boost::python::api::proxy<boost::python::api::attribute_policies> >::operator() (this=<optimized out>) at /home/BUILD64/lib/boost-1.69.0-py37/include/boost/python/object_core.hpp:440
python/cpython#51618 0x00002aaaabc8b287 in PyEDGInterface::py_backend (this=<optimized out>) at /home/Users/avj/vector/source/vc21__90601_pyedg_improvements/lib/libcommoncpp/src/PyEDGInterface.cpp:192
python/cpython#51619 0x00002aaaabc8c136 in PyEDGInterface::backend () at /home/Users/avj/vector/source/vc21__90601_pyedg_improvements/lib/libcommoncpp/inc/PyEDGInterface.h:38
python/cpython#51620 0x00000000004195b5 in back_end () at /home/Users/avj/vector/source/vc21__90601_pyedg_improvements/progs/pyedg/main.cpp:77
python/cpython#51621 0x000000000050ab21 in cfe_main (argc=argc@entry=9, argv=argv@entry=0x7fffffffd6c8) at /home/Users/avj/vector/source/vc21__90601_pyedg_improvements/progs/edg/src/cfe.cpp:141
python/cpython#51622 0x000000000050abda in edg_main (argc=argc@entry=9, argv=argv@entry=0x7fffffffd6c8) at /home/Users/avj/vector/source/vc21__90601_pyedg_improvements/progs/edg/src/cfe.cpp:202
python/cpython#51623 0x0000000000419752 in main (argc=9, argv=0x7fffffffd6c8) at /home/Users/avj/vector/source/vc21__90601_pyedg_improvements/progs/pyedg/main.cpp:43
