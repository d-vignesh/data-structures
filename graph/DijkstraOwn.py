
'''
	PYTHON MODULE TO IMPLEMENT A GRAPH DS AND DIJKSTRA ALGORITHM
'''


import logging
import collections
logging.basicConfig(level=logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')

# CLASS TO REPRESENT A VERTEX
class Vertex(object):
	def __init__(self, data):
		'''
			I/P  : DATA OF THE VERTEX
			RTN  : NONE
			OPTN : CONSTRUCTOR METHOD TO INITIALIZE VARIABLES
		'''
		self.data = data
		self.edges = []
		logging.debug(f' new vertex formed with data : {self.data}')

	def __str__(self):
		return str([(edge, dis) for edge, dis in self.edges])

# CLASS TO REPRESENT A GRAPH
class Graph(object):
	def __init__(self):
		'''
			I/P  : NONE
			RTN  : NONE
			OPTN : SCONSTRUCTOR METHOD TO INITIALIZE VARIABLES
		'''
		self.vertices = collections.defaultdict()


	def add_vertex(self, data):
		'''
			I/P  : DATA OF THE VERTEX
			RTN  : NONE
			OPTN : CREATES THE VERTEX OBJ WITH GIVEN DATA AND ADDS IT TO THE GRAPH
		'''

		vertx = Vertex(data)
		self.vertices[data] = vertx 
		logging.debug(f' the state of the graph after adding the vertex is :\n {self.vertices.keys()}')



	def add_edge(self, from_ver , to_ver , distance):
		'''
			I/P  : SOURCE VERTEX , END VERTEX AND DISTANCE OF THE EDGE
			RTN  : NONE
			OPTN : ADDS A NEW EDGE FROM FROM_VERTEX TO TO_VERTEX WITH GIVEN DISTANCE
		'''

		if from_ver in self.vertices and to_ver in self.vertices :
			# from to to 
			self.vertices[from_ver].edges.append((to_ver, distance))
			logging.debug(f'new edge added from {from_ver} to {to_ver} with distance {distance}')
			logging.debug(f'edges of {from_ver} is : {self.vertices[from_ver].edges}')
			
			# to to from 
			self.vertices[to_ver].edges.append((from_ver, distance))
			logging.debug(f'new edge added from {to_ver} to {from_ver} with distance {distance}')
			logging.debug(f'edges of {to_ver} is : {self.vertices[to_ver].edges}')

			return 'edge added'

		else :
			if from_ver not in self.vertices:
				return ' from_vertex is not in graph'
			else :
				return ' to_vertex not in graph'


	def display_graph(self):
		'''
			I/P  : NONE
			RTN  : NONE
			OPTN : PRINTS THE STATE OF THE GRAPH
		'''
		print(f'vertices : \n\t {str(self)}')
		print(f'edges :')
		for vertex in self.vertices :
			print(f'\tfrom {vertex} : {str(self.vertices[vertex])}')


	def __str__(self):
		return str([v for v in self.vertices])

	def dijkstra_shpath(self, src , des):
		'''

		'''

		# construct the visited dict, shortest path set and add the src_ver to them
		visited = {}
		shrtst_path = {}
		vertex_set = set(self.vertices)

		visited[src] = 0
		shrtst_path[src] = (0, [])

		path_found = False

		while(vertex_set):

			logging.debug(f'the visited vertices are : {visited.keys()}')
			logging.debug(f' vertices path to be computed are : {vertex_set}')
			logging.debug(f'the shortest path computed are : ')
			for path in shrtst_path :
				logging.debug(f'reach {path} from {shrtst_path[path][1]} in {shrtst_path[path][0]}')

			# traverse through the visited vertices and obtain the min_distance vertex available.
			min_vertex = None
			for vertex in vertex_set :
				if vertex in visited :
					if min_vertex == None :
						min_vertex = vertex
					elif visited[min_vertex] > visited[vertex]:
						min_vertex = vertex

			if min_vertex == des :
				path_found = True
				break  

			# remove the min_vertex from the vertex_set as its shortest path is the one currently obtained.
			vertex_set.remove(min_vertex)
			current_dis = visited[min_vertex]
			logging.debug(f' the min vertex chosen is : {min_vertex} with distance : {current_dis}')

			# traverse the adjacent verteices of min_vertex and add them to the visited dict.
			for adj_ver , dis in self.vertices[min_vertex].edges:
				d = current_dis + dis 
				if adj_ver not in visited:
					visited[adj_ver] = d
					logging.debug(f' the path list is : {shrtst_path[min_vertex][1]}')
					shrtst_path[adj_ver] = (d , shrtst_path[min_vertex][1] + [min_vertex])
					logging.debug(f'adding adjacent vertex : {adj_ver} at distance : {d}')
				elif visited[adj_ver] > d :
					visited[adj_ver] = d
					shrtst_path[adj_ver] = (d, shrtst_path[min_vertex][1] + [min_vertex])
					logging.debug(f'adding adjacent vertex : {adj_ver} at distance : {d}')

		#for path in shrtst_path :
			#print(f'{path} -- {shrtst_path[path][0]} | {shrtst_path[path][1]}')

		if path_found :
			print(f'{des} -- {shrtst_path[des][0]} | {shrtst_path[des][1]}')


class GraphAccess(object):
	
	def main():
		print('\t\t Dijkstra algo')
		cont = 'y'
		graph = Graph()

		while(cont=='y'):
			print('available options : \n\t 1.add_vertex \n\t 2.add_edge \n\t 3.dijkstra \n\t 4.display_graph')
			choice = input(' enter you choice : ')

			if choice == '1':
				data = input(' enter vertex data : ')
				graph.add_vertex(data)

			elif choice == '2':
				from_ver, to_ver , distance = input(' enter src vertec , distination ver and distance of the edge : ').split()
				print(graph.add_edge(from_ver, to_ver, int(distance)))

			elif choice == '3':
				src_ver, des_ver= input('Enter the src vertex : ').split()
				graph.dijkstra_shpath(src_ver, des_ver)

			elif choice == '4':
				graph.display_graph()

			cont =input(' do you want to continue (y/n) : ')

	if __name__ == '__main__':
		main()
