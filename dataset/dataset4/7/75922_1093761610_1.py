import sys
from os import getcwd
from os.path import join
sys.path.insert(0, join(getcwd(), 'MyLibraries'))

# Now if we import backports, we should find the one in our MyLibraries directory
import backports
print(backports.__path__)    # Nope... :(
# C:\Python27\lib\site-packages\backports

# What's weird is it's not entirely broken... you can do the following:
import chardet
print(chardet.__path__)
# Prints my path to MyLibraries/chardet
# So the path is correct and other libraries are coming in correctly