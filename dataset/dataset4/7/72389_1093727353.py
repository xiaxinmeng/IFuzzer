class Simple:
     def __init__( self ):
         print('Simple__init__')
     def __del__( self ):
         print('Simple__del__')

simple = None

def run():
    global simple
    simple = Simple()

if __name__ == '__main__':
	run()