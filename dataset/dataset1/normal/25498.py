from multiprocessing import Value
import argparse
import ipaddress
import logging.handlers
import datetime

class A: 
    def __init__(self, ref):
        self.ref = ref
         
class B: 
    def __init__(self):
        self.value = Value("b")
        self.ref = A(self)
         
def main():
    B()  
    return 
         
if __name__ == "__main__":
    exit(main())
         
         
         
         

