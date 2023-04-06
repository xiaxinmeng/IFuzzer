class Node( object ):
	pass


nodes = []
for i in range( 500 ):
	n = Node()
	nodes.append( n )

for n in nodes:
	n.connections = list( nodes )
	n.connections.remove( n )

import cPickle as pickle
pickle.dump( n, file( 'file', 'wb' ) )
print('ok')


