#from io import open
from _pyio import open

class MyClass:
   my_open = open

MyClass().my_open("document.txt", "w")