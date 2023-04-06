class Edge:
	def __init__(self, V1, V2):
		self.vertexes=[V1, V2]
		V1.edges.append(self)
		V2.edges.append(self)