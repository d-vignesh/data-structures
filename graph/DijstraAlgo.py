
import collections

'''
	PYTHON CODE TO IMPLEMENTATION OF DIJSTRA'S ALGORITHM
'''

class Graph(object):
	def __init__(self):
		'''
			I/P  : NONE
			O/P  : NONE
			OPTN : CONSTRUCTOR METHOD THAT INITIALIZES THE REQUIRED ATTRIBUTES OF THE GRAPH
		'''
		self.vertices = set()
		self.edges = collections.defaultdict(list)
		self.distances = {}

	def add_vertex(self, value):
		'''
			I/P  : THE VALUE WITH WHICH A VERTEX HAS TO BE ADDED
			O/P  : NONE
			OPTN : ADD A VERTEX WITH THE GIVEN VALUE TO THE vertices MEMBER
		'''
		self.vertices.add(value)

	def add_edge(self, from_vertex, to_vertex, distance):
		'''
			I/P  : THE VERTEX FROM WHICH THE EDGE ORIGINATES AND THE VERTEX IN WHICH THE EDGE ENDS AND THE WEIGHT OF THE EDGE AS DISTANCE
			O/P  : NONE
			OPTN : UPDATES THE edges MEMBER OF THE FROM AND TO VERTEICES ABOUT THE NEW ADJACENT VERTICES AND THE distances MEMBER WITH THE DISTANCE VALUE PROVIDED
		'''
		self.edges[from_vertex].append(to_vertex)
		self.edges[to_vertex].append(from_vertex)
		self.distances[(from_vertex, to_vertex)] = distance
		self.distances[(to_vertex, from_vertex)] = distance

def dijkstra(graph, src_v):
	visited = {src_v : 0}
	path = {}

	vertex_set = set(graph.vertices)

	while vertex_set :
		min_vertex = None
		for vertex in vertex_set :
			if vertex in visited :
				if min_vertex is None :
					min_vertex = vertex
				elif visited[vertex] < visited[min_vertex]:
					min_vertex = vertex

		print(min_vertex)

		if min_vertex is None:
			break
				
		vertex_set.remove(min_vertex)
		current_weight = visited[min_vertex]

		for edge in graph.edges[min_vertex]:
			weight = current_weight + graph.distances[(min_vertex, edge)]
			if edge not in visited or visited[edge] > weight :
				visited[edge] = weight
				path[edge] = min_vertex

		print(visited)		
	return visited, path


graph = Graph()
optn = 'y'

while(optn == 'y'):
	print('availabe options : \t\n 1.add_vertex \t\n 2.add_edge \t\n 3.dijstra shortest path')
	choice = input('enter your choice : ')
	if choice == '1':
		value = input(' enter the value of the vertex : ')
		graph.add_vertex(value)
	elif choice =='2':
		from_vertex, to_vertex, distance = input('enter the from_vertex, to_vertex, distance of the edge : ').split()
		graph.add_edge(from_vertex, to_vertex, int(distance))
	else :
		src_v = input('enter the source vertex : ')
		visited, path = dijkstra(graph, src_v)
		print(visited)
		print(path)



