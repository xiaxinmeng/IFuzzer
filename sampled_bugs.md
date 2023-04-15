In the following, we sample 26 reported bugs and present the details included bug ID, source code, the type of crash, interpreter versions, the description of these bugs. 


 

#####  1. CPython \#98354: create_builtin() in _imp module trigger segfault if taking a builtin object as input.

```python
1. import _imp
2. class FakeSpec:
3.  	def __init__(self, name):
4.  		self.name = self
5. A = FakeSpec("time")
6. imp_time = _imp.create_builtin(A)
```


<u>Crash</u>: Segmentation fault(core dumped)

<u>Python Version</u>: CPython 3.10.8

<u>Description</u>:
This Python code creates a object FakeSpec and uses the \_imp module to create a built-in module object for the "time". The FakeSpec class takes a module name as an argument and sets it as an attribute of the instantiated object. \_imp.create\_builtin() function is then used to create a built-in module object for the "time" module using the FakeSpec object created earlier. The create_builtin() function is a low-level function in the \_imp module that creates a built-in module object from a module specification object. However, in class FakeSpec, self.name is set to self leading to the CPython interpreter crashing. Developers have confirmed this bug to be unknown and fixed it.



##### 2. IronPython #1618 Memory leak when assigning to a bytearray via subscripting. 

```python
1. class X:
2.     def __index__(self):
3.         del b[0:0x10000]
4.         return 1
4. b = bytearray(b"A"*0x100)
5. b[::X()] = bytearray(b"B"*0x8000)
```

<u>Crash</u>: Aborted (core dumped)

<u>Python Version</u>: IronPython 3.4.0b1 

<u>Description</u>:
The code defines a class X with an \_\_index\_\_ method and creates a bytearray b of length 256 (0x100 in hexadecimal) containing the bytes "A". It then assigns the bytes "B" repeated 0x8000 (32768) times to a slice of b using the \_\_setitem\_\_ method with a step of the result of calling X(). In X(), it deletes b[0:0x10000] causing the memory leaking and finally crashing IronPython. Developers have confirmed this bug. 


##### 3. CPython \#96676: Union and isdisjoint operations between self-defined set classes cause segfault on CPython 3.12.0a0


```python
from collections.abc import Set
class MySet(Set):
    def __init__(a, itr):
        a.contents = a
    def __contains__(a, x):
        return a in a.contents
    def __iter__(a):
        return iter(a.contents)
    def __len__(a):
        return len([a for a in a.contents])
        
s1 = MySet((1, 2, 3))
s2 = MySet((3, 4, 5))
# s1 = s2 & s2       //crash, segmentation fault
s1.isdisjoint(s2)    // also crash, segmentation fault
```

<u>Crash</u>: Segmentation fault (core dumped)

<u>Python Version</u>: CPython 3.12.0a0


<u>Description</u>:
This code defines a custom class MySet that inherits from the abstract base class Set in the collections.abc module. The MySet class defines four methods: \_\_init\_\_(a, itr) initializes a MySet instance with the contents of the iterable itr. \_\_contains\_\_(a, x) returns True if x is in a.contents, which is the internal list storing the elements of the set. \_\_iter\_\_(a) returns an iterator over the elements in a.contents. \_\_len\_\_(a) returns the number of elements in a.contents.
The code then creates two instances of MySet: s1 with contents (1, 2, 3) and s2 with contents (3, 4, 5). If the next two lines of code, s1 = s2 & s2 and s1.isdisjoint(s2) were executed, they would raise a Segmentation fault. This is because the MySet class does not implement the required methods for set intersection (\_\_and\_\_()) and disjointness testing (isdisjoint()), which are inherited from the Set base class. In addition, the \_\_init\_\_ method does not correctly store the contents of the set, leading to errors when accessing its elements.





##### 4. Codon #244: Handling a self-defined error leads to the failure of codon

```python
1. class B:
2.     def __bool__(self):
3.         raise AttributeError("don't do that!")
4. b = B()
5. try:
6.    if b:
7.         pass
8. except AttributeError:
9.    print("HI")
```
   

<u>Crash</u>: Aborted (core dumped)

<u>Python Version</u>: Codon v0.15.5

<u>Description</u>:
The code defines a class B that has a single method \_\_bool\_\_, which raises an AttributeError with a message if it is called. Then, an instance b of class B is created. The code then attempts to evaluate the boolean value of b in an if statement by calling its \_\_bool\_\_ method. However, since the \_\_bool\_\_ method raises an AttributeError, this causes the try block to catch the exception and print "HI". Therefore, the expected output of running this code will be "HI". However, this case triggers a crash on Codon.


##### 5. CPython #88881, IronPython #1251: Incorrect arguments in function select() cause segfault.

```python
import select
def test_select_mutated():
    a = []
    class F:
       def fileno(a):
           del test_select_mutated()[-1]
           return sys.__stdout__.fileno()
    a[:] = [F()] * 10
    select.select([],a,[]),([],a[:5],[])

test_select_mutated()
```

<u>Crash</u>: Segmentation fault (core dumped)

<u>Python Version</u>: CPython 3.9.0

<u>Description</u>:
This bug is related to recursion crashing both CPython and IronPython. This program ends up with an unlimited number of iterations of select.select() and test_select_mutated() on the call stack. But the stack depth checker is not triggered, leading to the crashes of Python interpreters. Developers confirm this bug and claim that fixing this bug would require adding a stack depth check to the PyObject_Call family of functions. A pull request for fixing this bug may not be accepted due to the possible performance impact.

  





##### 6. CPython \#87053: 100000 assignments of .__sizeof__ cause a segfault on del


```python
mystr = "hello123"
for x in range(1000000):
    mystr = mystr.__sizeof__
    print(mystr)
```

<u>Crash</u>: Segmentation fault (core dumped)

<u>Python Version</u>: CPython 3.9.0

<u>Description</u>:
In this program, the attribute __sizeof__ of mystr is assigned to variable mystr  for 1,000,000 times. Then CPython interpreter crashes with segmentation fault. When __sizeof__ is assigned, a new object is allocated on the heap and returned to the caller. This new object also owns an attribute __sizeof__ that does the same operation. So the dealloc of mystr causes recursive calls to tp_dealloc along the entire chain, which exhausts the C stack. Developers confirm this is a hard bug. They are now in a heated discussion of the fix. It may not be easy to fix this bug completely. 


##### 7. gpython #202: Reassignment of 'getattr' leads to gpython crashing 

```python
1. class c(object):
2.     __getattr__ = getattr
3. c().spam
```


<u>Crash</u>: gpython crashes

<u>Python Version</u>: gpython 3.4.0

<u>Description</u>:The code defines a class c that has a single method \_\_getattr\_\_, which is set to the built-in function getattr. When an attribute of an instance of c is accessed using the dot notation (e.g., c().spam), Python first looks for the attribute on the instance itself. If it is not found, Python will call the \_\_getattr\_\_ method of the instance, passing the name of the attribute as a string. In this case, since \_\_getattr\_\_ is set to getattr, which returns the value of the requested attribute or raises an AttributeError if it doesn't exist, the code will simply return the value of the spam attribute of the instance of c. However, since the instance of c was created with no attributes, accessing any attribute with dot notation will raise an AttributeError. Instead of raising a AttributeErorr, gpython interpreter crashes.


##### 8. CPython #88882: Incorrect callable object crashes Python 3.11.0a0 

```python
import weakref

class Object:
    def __init__(self, arg):
        self.arg = arg

def test_set_callback_attribute():
    x = Object(1)
    callback = lambda ref: None
    callback = weakref.ref(callback, x)
    with test_set_callback_attribute():
        pass

test_set_callback_attribute()
```

<u>Crash</u>: Segmentation fault (core dumped) on CPython 3.11.0, Aborted (core dump) on CPython 3.9.0

<u>Description</u>: 
Running this program in debug mode can get a failed assertion at traceback.c. If that assertion is commented out, a null pointer is dereferenced in
\_PyPegen\_byte\_offset\_to\_character_offset(), And thus it crashes CPython. Developers have fixed this issue.


##### 9. PyPy #3864: incorrect recv in socket.socketpair leads to crashing

```python
1. import socket
2. (a, b) = socket.socketpair(socket.AF_UNIX, 
3. socket.SOCK_DGRAM)
4. a.send(b'abcdefgh')
5. result = b.recv(2, socket.MSG_TRUNC)
6. print(len(result), result)
```

<u>Crash</u>: Aborted (core dumped)

<u>Python Version</u>: pypy3.9-v7.3.10rc3 

<u>Description</u>: 
This Python code uses the socket module to create a pair of connected sockets and send a message between them using the User Datagram Protocol (UDP). The code sends the message b'abcdefgh' from the first socket a to the second socket b, and then receives a truncated message of up to 2 bytes from the second socket b and prints its length and contents. 



##### 10. CPython #86666:crash with unbounded recursion in except statement

```python
def status():
	try:
		1/0
	except status():
		pass
status()
```


<u>Crash</u>: Aborted (core dumped)

<u>Python Version</u>: CPython 3.9.0

<u>Description</u>:
This bug crashes all stable releases and pre-releases of CPython. Now it is fixed in the latest release of CPython after we report it. The root cause of this bug is related to recursion. In the implementation of CPython, once a program catches exceptions more than 50 + recursion limit times, the C stack overflows leading to the interpreter crashes. 
In this bug,  ZeroDivisionError is recursively raised and caught, and eventually makes it over the limit, causing CPython crashes. To fix this bug, developers replace the boolean state with the counter when handling soft overflows.







##### 11. PyPy #3523: Incorrect usage of ctype causes pypy crashing.


```python
1. from future import print_function
2. import ctypes
3. import ctypes.util
4. lib_location = ctypes.util.find_library('gettextpo')
5. gpo = ctypes.cdll.LoadLibrary(lib_location)
6. gpo_message = gpo.po_message_create()
7. source = 'foo'
8. print('calling po_message_set_msgid')
9. gpo.po_message_set_msgid(source, 10.source.encode('utf-8'))
11.print('success')
```

<u>Crash</u>: Segmentation fault (core dumped)

<u>Python Version</u>: PyPy 7.3.5 

<u>Description</u>: 
Incorrect usage of ctype causes pypy crashing, the developer claims that there are enough ways to crash Python with ctypes, and thus they are not sure whether they can fix this bug.


##### 12. CPython #87055: Incorrect behavior after ast node visits 

```python
1. import ast
2. class RewriteName(ast.NodeTransformer):
3.     def visit_BinOp(self, node):
4.         if node.left.value == 1:
5.             node.left = node
6.         return node
7. code = """
8. mystr  = 1 + (2+3)
9. """
10.myast = ast.parse(code)
11.transformer = RewriteName()
12.newast = transformer.visit(myast)
13.c = compile(newast,'<test>','exec')
14.exec(c)
```

<u>Crash</u>: Segmentation fault (core dumped)

<u>Python Version</u>: CPython 3.9.0

<u>Description</u>: 
In function visit_BinOp(), node.left is recursively assgined with a value of node,leading to crashes of CPython interpreter. Father of Python, Guido van Rossum confirms this bug. It may need a checker to check unsafe modification of AST.




##### 13. IronPython 1262. Recusive call of except branch in "yield from" crashes IronPython

```python
1. def foo():
2.     try:
3.         print(new)
4.         for i in range(100):
5.             yield i
6.     except:
7.         yield from foo()
8. m = foo()
9. for i in m:
10.    print(i)
```



<u>Crash</u>: crash

<u>Python Version</u>: IronPython 3.4.0a1 (3.4.0.0001) 

<u>Description</u>: 
This Python code defines a generator function called foo that uses a try-except block to catch an exception and recursively call itself using the yield from statement. The function is then called and iterated over in a loop using a generator object.  the code creates a generator function foo that yields numbers from 0 to 99, but raises a NameError exception before the loop starts. When the exception is caught, the function recursively calls itself and yields its own values. The generator object created by calling foo is then iterated over in a loop, printing each yielded value. Since the foo function is recursively called indefinitely when an exception is caught, the loop will continue indefinitely, and eventually lead to interpreter crashing. 



##### 14. CPython \#86883 The python interpreter crashed with "\_enter\_buffered\_busy"


```python
import threading
import warnings
class WarnOnDel(object):
   def __del__(self):
       warnings.warn("W", UserWarning)

def do_work():
    while True:
       w = WarnOnDel()

for do_work in range(10):
    t=threading.Thread(target=do_work)
    t.setDaemon(1)
    t.start()
``` 

<u>Crash</u>: Aborted (core dump) 

<u>Python Version</u>: CPython 3.9.0

<u>Description</u>:
This is a multi-threads program crashing CPython 3.7 - 3.10.  This program creates ten threads. target is assigned to function call do_work. Then in function do_work, warnOnDel is instanced in an endless loop.  target adopts an integer value for each thread, making the thread busy doing IO and holding the IO lock. Then to avoid a deadlock, the daemon threads are aborted during the shutdown. This crash can only be detected late on during interpreter shutdown, making the recovery work very hard. Besides, the thread termination has left the shared state in an unmanaged condition. So it is quite dangerous to re-enter Python again. 

##### 15. IronPython #1261: IronPython crashes when repr() handles too long nest dictionary 

```python
1. x = {}
2. for i in range(100000):
3.     x = {1: x}
4. repr(x)
```

<u>Crash</u>: crash

<u>Python Version</u>: IronPython 3.4.0a1 (3.4.0.0001)

<u>Description</u>: 
This Python code creates a dictionary x that contains nested dictionaries, where each key in the dictionary is mapped to the dictionary itself. The code iterates 100,000 times, each time creating a new dictionary where the key 1 maps to the previously created dictionary. Finally, the repr() function is called on x to return a string representation of the nested dictionary crashing InronPython.







##### 16. CPython \#89971: Importing asyncio after deleting a coroutine object and before cleaning it up leads to crashing on Python3.11

```python
1. async def f(): pass
2. f = f()
3. frame = f.cr_frame
4. del f
5. import asyncio
6. frame.clear()
```

<u>Crash</u>:Segmentation fault (core dumped)

<u>Python Version</u>: CPython 3.11.0a2+
 
 
<u>Description</u>: 
This program first defines an empty asynchronous function f(). Then it calls the function and assigns the result to a variable f. The next line retrieves the current frame object associated with the coroutine object f. It deletes the variable f, which means that there is no longer any reference to the coroutine object created by f(). The final two lines of the code import the asyncio module and call the clear() method on the frame object retrieved earlier. This method call removes all local variables from the frame object leading to the CPython interpreter crashing.
After  heated discussion of this bug, the developers have confirmed and fixed it by adding a Null checker for the generator pointer when deallocated, and dropping redundant assertions from frame.clear(). In total, this bug report has been reopened three times.



##### 17. IronPython #1259: IronPython gets crashing when rebinding \_\_repr\_\_ as \_\_str\_\_ 

```python
1. class Foo(object):
2.     pass
3. Foo.__repr__ = Foo.__str__
4. foo = Foo()
5. str(foo)
```

<u>Crash</u>: crash

<u>Python Version</u>: IronPython 3.4.0a1 (3.4.0.0001)

<u>Description</u>: 
This Python code defines a class Foo that inherits from the built-in object class and then sets its \_\_repr\_\_ method to be the same as its \_\_str\_\_ method. It then creates an instance of Foo called foo and calls the str() function on it causing IronPython crashing.


##### 18. gpython \#203: Annotating types with decorators crashes gpython

```python
1. class Link(str):
2.     p_name = None
3.     @p_name
4.     def fname(self) -> str:
5.         return self.p_name 
```

<u>Crash</u>: panic

<u>Python Version</u>: gpython 3.4.0
  
<u>Description</u>:
This program defines a class Link. In the class Link, the variable p\_name is assigned to None. The decorated function fname is annotated with the type str. However the type str is not consistent with the type None triggering the gpython interpreter crashes. The developer confirms that the root cause of this bug is an unchecked type assertion at the file "gpython/vm/eval.go" of the gpython interpreter. They are working on the fix of this bug. 

 

##### 19. RustPython \#2779: Raising a user-defined class from itself causes interpreter crashing

```python
1. class Error(Exception):
2.     pass
3. e = Error()
4. raise e from e 
```

<u>Crash</u>: Segmentation fault (core dumped)

<u>Python Version</u>: Rust Python 0.1.2 interpreter

<u>Description</u>:
This program defines a custom exception class Error, creates an instance of this class named e, and then raises this exception with the raise statement. The from keyword specifies that the exception being raised is caused by the exception itself, i.e. e. This program cause a segmentation fault on the RustPython interpreter. The root cause lies in the the implementation of the write\_exception for the raise operation in the file `vm/src/exceptions.rs'. The developer have confirmed this bug and fixed it.


##### 20. CPython \#97591: Setting state of an exception object with a dic crashes Python 3.8.14

```python
1. class C(str):
2.     def __hash__(self):
3.         d.clear()
4.         return 0
5. d = {}
6. d[C()] = C()
7. e = Exception()
8. e.__setstate__(d)

```

<u>Crash</u>: Segmentation Fault (Core dumped)

<u>Python Version</u>:  Python 3.8.14

<u>Description</u>:
This program defines a class C, in which a function \_\_hash\_\_() is defined to clear the content of the dictionary d. Then the dictionary is created and initialized with the instance of the class C. When taking the argument of the function Exception.\_\_setstate\_\_() as the dictionary d, CPython gets a segmentation fault. 
The developer claims the root cause of this bug is the function BaseException\_setstate() in the file `Python/exceptions.c'. The variable INCREF is missing  before calling tp\_hash slot in PyObject\_SetAttr. Developers fix this bug by acquiring strong reference before calling tp\_hash slot in Exception.\_\_setstate\_\_(). 





##### 21. Codon #247: Returning the position of a null file pointer causes a segfault

```python
1. with open('x', 'w') as f:
2.     f.write('xxx')
3. print(f.tell())
```

<u>Crash</u>: Segmentation fault (core dumped)

<u>Python Version</u>: Codon v0.15.5

<u>Description</u>:
This code will open a file named 'x' in write mode using the open() function, and assign the resulting file object to the variable f. The 'w' mode will truncate the file if it already exists, or create it if it doesn't. The write() method is then called on the f object to write the string 'xxx' to the file. Finally, the tell() method is called on the f object, which returns the current position of the file pointer, i.e., the position in the file where the next read or write operation will occur. In this case, since the last operation was a write, the file pointer will be at the end of the file, so the tell() method will return the number of characters in the file, which is 3 in this case.



##### 22. CPython \#88883: Weakref proxy crashes on null tp_iternext slot.

```python
1. import weakref
2. def test_proxy_iter():
3.     obj = None 
4.     class MyObj:
5.        def __iter__(a):
6.            nonlocal obj
7.            del obj
8             return p
9      obj = MyObj()
10.    p=weakref.proxy(TypeError)
11.    'blech' in obj
12. test_proxy_iter()

```
 
<u>Crash</u>: segmentation fault

<u>Python Version</u>: CPython 3.11.0a0
 
<u>Description</u>:
This program defines a function test\_proxy\_iter() and then calls it.
Function call weakref.proxy() returns a proxy of the  TypeError which uses a weak reference. When the argument of weakref.proxy() is not an iterator, the CPython interpreter crashes. We reported this bug to the developers. Developers have confirmed and fixed this bug in two days.    

##### 23. RustPython #4318:atexit.register() takes exited function causing rustpython panicked

```python
1. def myexit():
2.     import sys
3.     sys.exit(2)
4. import atexit
5. atexit.register(myexit)
```

<u>Crash</u>: panicked

<u>Python Version</u>: rustpython 0.1.2

<u>Description</u>:
This code defines a function called myexit() that imports the sys module and calls its exit() function with an exit code of 2. It then uses the atexit module to register myexit() as a function to be called when the Python interpreter is shutting down.
So when the program is running and it reaches the end, or when the program is interrupted, the function myexit() will be called with the exit code of 2, which will cause the program to exit with that status code. The atexit module allows you to register functions to be called automatically when a Python script is about to exit, regardless of whether it exits normally or due to an error.


##### 24. CPython \#97592: Bugs in asyncio.Future.remove_done_callback() cause segfault.

```python
1. import asyncio
2. fut = asyncio.Future()
3. fut.add_done_callback(str)
4. for str in range(63):
5.     fut.add_done_callback(id)
6. class evil:
7.     def __eq__(self, other):
8.        fut.remove_done_callback(other)
9. fut.remove_done_callback(evil())
```

<u>Crash</u>: Segmentation fault (core dumped)

<u>Python Version</u>:  CPython 3.9.0

<u>Description</u>:
This program creates an asyncio.Future() object fut. Then it constantly adds the callback to the object fut. Finally, it removes the callback by the class evil, crash the CPython interpreter. 
The developer has confirmed and fixed this bug. The root cause is that the call PyObject\_RichCompareBool invokes the evil class's \_\_eq\_\_ method, which calls the same function and ends up clearing fut\_callbacks. Developers fix this bug by adding checks for whether fut\_callbacks is NULL before doing anything further to it.







##### 25. RustPython 4319 Multiple 'for' loop make rustpython panicked.

```python
1. class F:
2.     def a(self):
3.        x = None
4.        x = [[(x_1 := 2) for self in range(2)] for x in range(2)]
5.        print(x, self)
6. F().a()
```


<u>Crash</u>: panicked

<u>Python Version</u>: rustpython 0.1.2

<u>Description</u>:
The above code defines a class F with a method a(). When an instance of F is created and its a() method is called, the method creates a variable x and sets it to None. Then it creates a list comprehension using x and self as iteration variables, with x\_1 := 2 as the expression being evaluated for each iteration.
The := operator is an assignment expression introduced in Python 3.8 that allows you to assign a value to a variable as part of an expression. In this case, x\_1 := 2 assigns the value 2 to the variable x\_1, and the resulting value of the expression is also 2.
So, the list comprehension [[(x\_1 := 2) for self in range(2)] for x in range(2)] creates a 2x2 list with the value 2 in each position.
Finally, the method a() prints out the resulting list and the value of self, which in this case is the instance of the F class that the method was called on. So the output of calling F().a() will be:
[[2, 2], [2, 2]] <\_\_main\_\_.F object at 0x...>
where the ... represents a memory address.


##### 26. IronPython #1616:Applying for-in structure in 'yield from' crashes ironpython.

```python
1. def test(b):
2.     obj = range(10)
3.     yield from (b for x in range(10))
```
    
<u>Crash</u>: Aborted (core dumped)

<u>Python Version</u>: IronPython 3.4.0b1 

<u>Description</u>:    
The provided code defines a Python function called test that takes a single parameter b. The function creates a generator object that yields values from an iterable object of integers created using the range function.

The yield from statement is used to delegate the iteration of the iterable (b for x in range(10)) to the generator object. This means that when the test function is called, it will return a generator object that can be iterated over to produce values.

The generator object will produce the value of b ten times because the range function is being used to iterate ten times. However, the value of b remains constant throughout the iteration.


