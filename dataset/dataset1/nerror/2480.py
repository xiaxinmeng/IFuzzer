class Node( object ):
	pass


nodes = []
for i in range( 250 ):
	n = Node()
	nodes.append( n )

for n in nodes:
	n.connections = set( nodes )
	n.connections.remove( n )

import pickle
pickle.dump( n, file( 'file', 'wb' ) )
print('ok')


