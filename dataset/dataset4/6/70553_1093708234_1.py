#!/usr/bin/python
import os

def main():
    product_dir ="/zope/eggs43"
    my_tuple= os.path.split(product_dir)[:-1]
    product_prefix = os.path.join(my_tuple )
    
if __name__ == "__main__":
    main()