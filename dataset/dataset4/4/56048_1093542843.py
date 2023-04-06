import argparse 
parser = argparse.ArgumentParser() 
parser.add_argument( 
"-o", 
default = 'fake', 
dest = 'OutputFile', 
type = argparse.FileType('w') 
) 
args = parser.parse_args() 