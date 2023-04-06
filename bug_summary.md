#A summary of the reported bugs.
This document provides a summary of reported bugs that have been detected using IFuzzer. 

The bug list is continuously updated as more bugs are found. We have tested 11 Python interpreters/compilers with IFuzzer, which include CPython, IronPython, RustPython, PyPy, Jython, gpython, Pyston, Codon, GraalPython, and MicroPython. The detected bugs demonstrate the effectiveness of IFuzzer. We also attempt to test other code analysis tools with IFuzzer, such as MyPy, and have found promising results. Unknown bugs have been detected through this process.

You can verify the reported bugs through the bug IDs provided in the second column of the table in the issue trackers of these Python interpreters. The list of the every Python Issue Tracker is given in the end of this document.



#### CPython:
This is the standard and most widely used implementation of the Python programming language. It is written in C and executes Python code using an interpreter. CPython includes a large standard library and is compatible with many third-party libraries and tools. 


|  ID   | BugID  | Title | Status |Stage | Confirmed|
|  ----  | ----  | ----  | ----  | ----  | ---- |
1|101928|Multi-line arguments in a function call crashes CPython|closed|fixed|confirmed
2|98354|create_builtin() in \_imp module trigger segfault if taking a builtin object as input|closed|fixed|confirmed
3|97592|Bugs in asyncio.Future.remove_done_callback() cause segfault.|closed|fixed|confirmed
4|97591|Setting state of an exception object with a dic crashes Python 3.8.14|closed|fixed|confirmed
5|96676|Union and isdisjoint operations between self-defined set classes cause segfault on CPython 3.12.0a0|open||confirmed
6|90369|Recursively calling makepasv() finally leads to core dumped.|open||open
7|90273|Interrupting subprocess.popen in recursive calls by KeyboardInterrupt causes Fatal Python error.|open||open
8|90018|Mutithread leads to Illegal instruction crashing CPython|open||open
9|89984|unittest.assertRaisesRegex is broken in Python 3.11 and leading to crashing if tested regex does not match name.|closed|fixed|confirmed
10|89971|Importing asyncio after deleting a coroutine object and before cleaning it up leads to crashing on Python3.11|closed|fixed|confirmed
11|88883|Weakref proxy crashes on null tp_iternext slot.|closed|fixed|confirmed
12|88882|Incorrect callable object crashes Python 3.11.0a0|closed|fixed|confirmed
13|88881|Incorrect arguments in function select() cause segfault|open||confirmed
14|87830|Compiling long expression leads to segfault (again)|closed|duplicate|invalid
15|87765|Setting long domain of locale.dgettext() crashes Python interpreter|open||confirmed
16|87356|< test.support > check_free_after_iterating( ) causes core dump in handling iteration.|closed|duplicate|invalid
17|87355|<test.support> decorator function run_with_locale() crashes Python interpreter|closed|duplicate|invalid
18|87354|<dict> multiple operations of dict causes core dump of Python interpreter.|closed ||confirmed
19|87353|Dict creation in recursive function cause interpreter crashes.|closed||confirmed
20|87352|Recursive call causes core dump in assertRaises|closed|duplicate|invalid
21|87351|<unittest> AssertRaises() causes core dump in handling recursion|closed||confirmed
22|87247|Recursive call crash module multiprocessing|open||open
23|87117|"Random and infinite loop in dealing with recursion error for ""try-except """|closed|not a bug|invalid
24|87116|Incorrect exception behavior in handling recursive call.|open||open
25|87084|"Nested multi-line expression will lead to ""compile()"" fails"|closed|fixed|confirmed
26|87055|Incorrect behavior after ast node visits|closed||confirmed
27|87054|Not installed \_\_ibgcc\_s.so.1\_ causes exit crash.|closed|fixed|confirmed
28|87053|100000 assignments of .\_\_sizeof\_\_ cause a segfault on del|open||confirmed
29|87023|"Fails to construct paths lead to ""python is likely shutting down"""|closed|wont fix|confirmed
30|86929|"Exposing a race in the ""\_warnings"" resulting Python parser crash"|closed|duplicate|invalid
31|86928|"infinite loop resulted by ""yield"""|open||open
32|86901|"""trace_at_recursion_limit.py"" should be removed from ""Python/Lib/test/crashers"""|open||open
33|86900|"Outdated CodeType call in ""bogus_code_obj.py"""|closed|fixed|confirmed
34|86883|"The python interpreter crashed with ""_enter_buffered_busy"""|open||confirmed
35|86878|Segmentation fault in running ast.literal_eval() with large expression size.|closed|duplicate|invalid
36|86818|recursive in finally clause cause Python interpreter crash.|closed|fixed|confirmed
37|86817|Recursive traceback crashes Python Interpreter|closed|fixed|confirmed
38|86675|Recursive calls crash interpreter when checking exceptions|closed|duplicate|invalid
39|86666|crash with unbounded recursion in except statement|closed|fixed|confirmed
40|81899|2to3 exception handling|closed|wont fix|confirmed
41|81896|2to3 set default encoding|closed|wont fix|confirmed






#### IronPython
 IronPython is an implementation of Python that is designed to run on the .NET Framework. It allows Python code to be executed within a .NET environment and can interact with other .NET languages such as C# and VB.NET. IronPython is often used in applications that require integration with the .NET platform.

|  ID   | BugID  | Title | Status |Stage | Confirmed|
|  ----  | ----  | ----  | ----  | ----  | ---- |
1|1250|Global \_\_class\_\_ statement in class declaration leads to InvalidCastException|closed|fixed|confirmed
2|1251|Incorrect argument in function select() causes stack overflow|open||confirmed
3|1252|Incorrect usage of ctype causes ironpython crashing.|open||confirmed
4|1253|Infinite loop causes Null Reference Exception of ironpython|open||confirmed
5|1254|Function truncate() causes core dumped.|open||confirmed
6|1255|isinstance accepts subtypes of tuples as second argument causing segfault|closed|fixed|confirmed
7|1258|Recursive setting attributes causes IronPython crashing|closed||confirmed
8|1259|IronPython gets crashing when rebinding \_\_repr\_\_ as \_\_str\_\_|open||confirmed
9|1260|Transforming a long list cause IronPython crashes|open||confirmed
10|1261|IronPython crashes when repr() handles too long nest dictionary|open||confirmed
11|1262|"Recusive call of except branch in ""yield from"" crashes IronPython"|open||confirmed
12|1263|Recursive function call crashes IronPython|closed|duplicate|invalid
13|1264|Running compile() with large size expression crashes IronPython|open||confirmed
14|1265|Recusive instance in dict causes IronPython crashing.|open||confirmed
15|1606|"Ironpython reports ""No module named 'stat'"" when failing importing os module"|closed|duplicate|invalid
16|1607|Recursively adding handler in log.addHandler() crashes ironpython|closed|not a bug|invalid
17|1608|Changing \_\_bases\_\_ attribute in issubclass() causes core dumped|open||confirmed
18|1609|Setting attribute to 'self' in unittest.mock.patch crashes ironpython|closed|not a bug|invalid
19|1610|unittest.mock.Mock crashes ironpython|closed|not a bug|invalid
20|1613|Transforming types of loop condition in 'for' crashes ironpython|open||confirmed
21|1614|Specific string format causes crashes|closed|fixed|confirmed
22|1615|DefaultSelector().select() in selectors module fails on ironpython|closed|fixed|confirmed
23|1616|Applying for-in structure in 'yield from' crashes ironpython.|open||confirmed
24|1617|Long string in Tokenlist of email.policy crashes Ironpython|closed|fixed|confirmed
25|1618|Memory leak when assigning to a bytearray via subscripting.|open||confirmed


#### PyPy

PyPy is a fast| alternative implementation of Python. It uses a Just-In-Time (JIT) compiler to speed up execution of Python code. PyPy can be used as a drop-in replacement for CPython| but it may not be compatible with all third-party libraries.

|  ID   | BugID  | Title | Status |Stage | Confirmed|
|  ----  | ----  | ----  | ----  | ----  | ---- |
1|3482|Setting long domain of locale.dgettext() crashes PyPy|closed||confirmed
2|3504|Recursive call causes semaphores leak in multiprocess|open|not a bug|invalid
3|3505|Pypy: os.fork() causes memory leak in recursively call and crashing Pypy and Ubuntu OS.|open||open
4|3522|mmap() causes bus error upon resizing file|open||open
5|3523|ctype: Incorrect usage of ctype causes pypy crashing.|open||confirmed
6|3529|Decimal division get stuck with max_prec precision|open||open
7|3863|Taking invalid class name in tkinter.Tk crashes PyPy|open||open
8|3864|incorrect recv in socket.socketpair leads to crashing|open|patch|confirmed


#### Jython

Jython is an implementation of Python that is designed to run on the Java Virtual Machine (JVM). It allows Python code to be executed within a Java environment and can interact with other Java code. Jython is often used in applications that require integration with Java libraries or frameworks.



|  ID   | BugID  | Title | Status |Stage | Confirmed|
|  ----  | ----  | ----  | ----  | ----  | ---- |
1|109|The lack of type initialization causes Jython crashing.|open||open
2|110|Jython crashes when running ast.parse() with large expression size|open||open
3|111|"ctypes.CDLL(""libgcc_s.so.1"") causes java.lang.UnsatisfiedLinkError"|closed|not a bug|invalid
4|112|Long string computation crashes Jython|open||open
5|113|ctypes causes IllegalStateException of Jython|closed|wont fix|confirmed
6|114|Unfound SAXParser crashes Jython|closed||invalid
7|115|Misuse of slice crashes Jython|open||confirmed
8|116|exec() takes too long computation crashes Jython|open||open
9|117|Inconsistent behavior of nonlocal between CPython and Jython|closed|not a bug|invalid
10|118|sort() cause jython crashing with java.lang.NullPointerException|open||open

#### RustPython

RustPython is a new implementation of Python that is written in Rust| a systems programming language known for its speed and safety features. RustPython is still in development| but it aims to be faster and more memory-efficient than CPython.


|  ID   | BugID  | Title | Status |Stage | Confirmed|
|  ----  | ----  | ----  | ----  | ----  | ---- |
1|2778|Rust Python gets crashing when rebinding \_\_repr\_\_ as \_\_str\_\_|closed|fixed|confirmed
2|2779|Raising a user-defined class from itself causes interpreter crashing|closed|fixed|confirmed
3|2780|Segmentation fault in running compile() with large expression size.|closed||confirmed
4|2781|Evaluating a long list with eval() causes segfault|closed||confirmed
5|2782|repr() of deeply nested dicts and dictviews can cause a stack overflow.|closed||confirmed
6|2783|exec() crashes Rust Python when taking large expression as argument|closed||confirmed
7|3456|Appending list too many times crashes RustPython|closed|invalid|invalid
8|4312|"Checking unmatched ""raiseregex"" leads to rustpython panicked"|closed|fixed锛_ood first issue|confirmed
9|4313|Nest call function in threads cause Illegal instruction in Thread|open||
10|4314|Setting locals() value leads to panicked.|open|fixed|confirmed
11|4315|Removing list with index 0 causes panicked.|closed|fixed|confirmed
12|4316|Extra argument in compile() leads to panicked.|closed|fixed|confirmed
13|4317|Starmapping too many times crashes rustpython.|open|not a bug|invalid
14|4318|atexit.register() takes exited function causing rustpython panicked|closed|fixed锛_ood first issue|confirmed
15|4319|Multiple 'for' loop make rustpython panicked.|closed|fixed|confirmed
16|4427|mmap() triggers a segfault upon resizing the underlying file|open||confirmed
17|4428|panicked in handling multiple free in sqlite3|open||confirmed
18|4429|panicked when output buffer is resized too many times|closed|fixed|confirmed
19|4430|segfault in deleting attributes recursively in sqlite3|open||confirmed
20|4848|Panicked when using annotation with beartype|open||confirmed

#### Pyston

Pyston is an alternative implementation of Python that is designed for high performance. It uses a Just-In-Time (JIT) compiler to speed up the execution of Python code. Pyston is compatible with most Python code and libraries| but may not be compatible with some C extensions.

|  ID   | BugID  | Title | Status |Stage | Confirmed|
|  ----  | ----  | ----  | ----  | ----  | ---- |
1|291|Recursive call in 'traceback' module crashes pyston|open||confirmed
2|292|Failing to write a object with shelve module produces crashes on pyston|open||open
3|293|Throwing an exception class crashes pyston|open||open
4|294|Use a cleared index crashes|open||open
5|295|Recursively calling a function in 'try' branch cause core dumped|open||open
6|296|Recursive call causes segmentation fault when building a weakref|open||confirmed
7|299|Incorrect garbage collections crash pyston|open||confirmed

#### gpython

gpython is a Python interpreter that is implemented in Go| a modern programming language known for its simplicity and speed. gpython is designed to be lightweight and fast| making it a good choice for applications where performance is a priority.

|  ID   | BugID  | Title | Status |Stage | Confirmed|
|  ----  | ----  | ----  | ----  | ----  | ---- |
1|142|set(range(100)) behaves different with CPython and crashes gpython|closed|not a bug|invalid
2|143|Recursive call crashes gpython|open||confirmed
3|202|Reassignment of 'getattr' leads to gpython crashing|open||confirmed
4|203|Annotating types with decorators crashes gpython|open|good first issue|confirmed
5|204|__import__' takes incorrect arguments crashing gpython|open||confirmed
6|205|Comparing uncomparable types in 'is' crashes gpython|open||confirmed
7|206|Transforming unsupported types into a set leads to crashing|open||open
8|207|Defining Nested set crashes gpython|open||confirmed
9|208|transforming generators into list trigger crashing|open||open
10|209|Taking large arguments in functions crashes gpython|open||open
11|210|Compiling long operations crashes gpython|open||open

#### Codon

Codon is a high-performance Python compiler that compiles Python code to native machine code without any runtime overhead. Typical speedups over Python are on the order of 10-100x or more| on a single thread. Codon's performance is typically on par with (and sometimes better than) that of C/C++. Unlike Python| Codon supports native multithreading| which can lead to speedups many times higher still. Codon grew out of the Seq project.

|  ID   | BugID  | Title | Status |Stage | Confirmed|
|  ----  | ----  | ----  | ----  | ----  | ---- |
1|229|Deleting the variable for-loop leads to a core dumped|open||confirmed
2|230|A fail of type check of a list causes a core dumped|open||invalid
3|231|"Type not set for unary ""-"" leads to a crash"|open||confirmed
4|232|"Open two file with nest ""with"" statement causes a core dumped"|open||open
5|233|Deleting not found file leads to crashing|open||invalid
6|239|Segmentation fault when importing a unknown module from the current directory|open||open
7|240|"Recursively calling a function in ""try"" branch leads to segfault"|open||open
8|241|"Function ""filter"" fails when the type of the first argument is not bool"|open||open
9|242|Transferring a list into a tuple fails on codon|open||open
10|243|Invoking type() twice causes a failure of codon|open||open
11|244|Handling a self-defined error leads to the failure of codon|open||confirmed
12|246|"Segmentation fault in invoking list(zip())"|open||open
13|247|Returning the position of a null file pointer causes a segfault|open||confirmed
14|249|Segmentation fault when taking a lambda function as the value of a dictionary|open||confirmed
15|253|typing.Tuple[int] fails codon when it is taken as a base class|open||confirmed
16|254|"re.compile() cannot identify operator ""(?<"""|open||invalid

#### MicroPython

MicroPython is a Python implementation that is optimized for microcontrollers and other embedded systems. It is designed to be fast and memory-efficient| and can be used to control hardware directly using Python code.

|  ID   | BugID  | Title | Status |Stage | Confirmed|
|  ----  | ----  | ----  | ----  | ----  | ---- |
1|10958|micropython get segfault when pow() takes the 3rd argument as 0|open||confirmed
2|10959|Clearing a existing dic object leads to Floating point exception|open||open
3|10960|Calling sys.stdin.close() causes a segmentation fault.|open||open
4|10961|"Passing a keyword argument to a subclass of the built-in class ""set"" causes a crash."|open||open

#### GraalPython

GraalPython is an implementation of Python that is built on top of the GraalVM| a high-performance virtual machine for running multiple languages. GraalPython uses the Truffle framework to provide high performance and support for dynamic language features.

|  ID   | BugID  | Title | Status |Stage | Confirmed|
|  ----  | ----  | ----  | ----  | ----  | ---- |
1|311|Instancing a manager in multiprocessing module crashes graalpython|open||confirmed
2|312|Building a pool in the multiprocessing module crashes graalpython|closed||invalid
3|313|Incorrect ctype mapping leads to java.lang.IllegalStateException|closed|fixed|confirmed
4|314|Overwritten mmap files triggers a segfault|closed||invalid



#### Pyjion

Pyjion is an experimental JIT compiler for CPython that is built on top of the .NET runtime. It uses the .NET runtime's Just-In-Time compiler to speed up the execution of Python code. Pyjion is still in development and is not yet recommended for production use.

|  ID   | BugID  | Title | Status |Stage | Confirmed|
|  ----  | ----  | ----  | ----  | ----  | ---- |
1|496|Using those freed variables in a class methods crashes pyjion|open||open
2|497|Recursive function call with functools.lru_cache produces segfault.|open||open


#### MyPy 
MyPy is not a Python interpreter| but rather a static type checker for Python. It allows developers to annotate their Python code with type hints| which can help catch errors at compile time instead of at runtime.

|  ID   | BugID  | Title | Status |Stage | Confirmed|
|  ----  | ----  | ----  | ----  | ----  | ---- |
1|14345|Incorrect asynchronous comprehension cause an internal error|closed|fixed|confirmed


#### List of Python Issue Trackers:
CPython: https://github.com/python/cpython/issues

IronPython: https://github.com/IronLanguages/ironpython3/issues

RustPython: https://github.com/RustPython/RustPython/issues

PyPy: https://foss.heptapod.net/pypy/pypy/-/issues/3864 

Jython: https://github.com/jython/jython/issues

gpython: https://github.com/go-python/gpython/issues

Pyston: https://github.com/pyston/pyston/issues

Codon: https://github.com/exaloop/codon/issues

GraalPython: https://github.com/oracle/graalpython/issues

MicroPython: https://github.com/micropython/micropython/issues

MyPy: https://github.com/python/mypy/issues