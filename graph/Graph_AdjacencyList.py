
'''
	python code to implement graph datastructure.
'''

import sys

class Graph(object):


	def __init__(self, graph_dict = None):
		'''
			INPUT 		: A DICTIONARY WITH KEY AS GRAPH VERTICES AND VALUE AS ADJACENT VERTICES / NONE
			OUTPUT 		: NONE 
			OPTN 	    : INITIALIZATION OF THE GRAPH OBJECT 
						  IF A DICTIONARY IS PROVIDED , INITIALIZES WITH IT OR WITH AN EMPTY DICT 
		'''

		if graph_dict == None :
			self.graph_dict = None

		self.graph_dict = graph_dict

	
	def list_vertices(self):
		'''
			INPUT 	: NONE
			OUTPUT	: A LIST OF ALL THE VERTICES PRESENT IN THE GRAPH
			OPTN  	: CONSTRUCTS A LIST OF ALL THE VERTICES IN THE GRAPH AND RETURN IT
		'''

		return self.graph_dict.keys()

	
	def list_edge(self):
		'''
			I/P  : NONE
			O/P  : A LIST OF TUPLES REPRESENTING ALL THE EDGES IN THE GRAPH
			OPTN : CALL THE generate_edge() AND RETURNS THE LIST OF THE EDGES 
		'''

		return self._generate_edge()

	
	def _generate_edge(self):
		'''
			I/P  : NONE
			O/P  : A LIST OF TUPLES REPRESENTING ALL THE EDGES IN THE GRAPH
			OPTN : CONSTRUCTS A LIST OF TUPLE WHERE EACH TUPLE REPRESENT AN EDGE 
				   BETWEEN THE TWO VERTICES IN THE TUPLE
		'''

		edges = []
		for vertex in self.graph_dict:
			for neighbour in self.graph_dict[vertex]:
				edges.append((vertex, neighbour))

		return edges

	
	def add_vertex(self, vertex):
		'''
			I/P  : DATA FOR THE VERTEX TO ADD
			O/P  : NONE
			OPTN : IF THE VERTEX IN NOT PRESENT IN THE GRAPH ADDS IT 
		'''

		if vertex not in self.graph_dict.keys():
			self.graph_dict[vertex] = []

	
	def add_edge(self, from_to_tuple ):
		'''
			I/P  : A TUPLE CONTAINING THE FROM AND TO VERTICES OF THE EDGE
			O/P  : NONE 
			OPTN : ADDS THE EDGE TO THE VERTEX BY UPDATING THE CONNECTIVITY INFORMATION
				   ON THE CORRESPONDING TWO VERTEX KEYS 
		'''

		vert1, vert2 = from_to_tuple
		vertecies = self.graph_dict.keys()
		if vert1 not in vertecies :
			self.graph_dict[vert1] = [vert2]
		else :
			self.graph_dict[vert1].append(vert2)


		if vert2 not in vertecies :
			self.graph_dict[vert2] = [vert1]
		else :
			self.graph_dict[vert2].append(vert1)


	def print_graph(self):
		'''
			I/P : NONE 
			O/P : A STRING REPRESENTATION OF THE GRAPH STATE
		'''
		return str(self)

	def __str__(self):
		'''
			I/P  : NONE
			O/P  : A STRING OBJECT REPRESENTING THE STATE OF THE GRAPH
			OPTN : CONTRUCTS A STRING OBJECT WITH ALL THE VERTICES AND EDGES IN THE GRAPH AND RETURNS IT
		'''

		result = ' vertices :'
		
		result += '\n\t' + str(list( self.graph_dict.keys()))

		result += '\n edges : '

		result += '\n\t' + str(self._generate_edge())

		return result

	def find_path(self, start_vertex, end_vertex):
		'''
			I/P  : THE START VERTEX AND END VERTEX FOR WHICH THE PATH MUST BE FOUND
			O/P  : A LIST CONTAINING THE PATH OR 'None' IF THERE IS NO PATH B/W THE GIVEN VERTICES
			OPTN : CALLS THE _find_path() to compute the path
		'''

		return self._find_path(start_vertex, end_vertex)


	def _find_path(self, start_vertex, end_vertex, path=[]):
		'''
			I/P  : THE START VERTEX AND END VERTEX FOR WHICH THE PATH MUST BE FOUND
			O/P  : A LIST CONTAINING THE PATH OR 'None' IF THERE IS NO PATH B/W THE GIVEN VERTICES
		'''
		
		path = path + [start_vertex]
		if start_vertex == end_vertex:
			return path

		if start_vertex not in self.graph_dict:
			return None

		for vertex in self.graph_dict[start_vertex]:
			
			if vertex not in path :
				extended_path = self._find_path(vertex, end_vertex, path)

				if extended_path :
					return extended_path
		return None


	def find_all_path(self, start_vertex, end_vertex):
		return self._find_all_path(start_vertex, end_vertex, path=[])
	

	def _find_all_path(self, start_vertex, end_vertex, path=[]):
		'''
			I/P  : THE START VERTEX AND END VERTEX FOR WHICH THE PATH MUST BE FOUND
			O/P  : A LIST CONTAINING THE PATH OR 'None' IF THERE IS NO PATH B/W THE GIVEN VERTICES
		'''

		path = path + [start_vertex]
		if start_vertex == end_vertex:
			return [path]

		if start_vertex not in self.graph_dict:
			return []

		paths = []
		for vertex in self.graph_dict[start_vertex]:
			
			if vertex not in path :
				extended_path = self._find_all_path(vertex, end_vertex, path)

				
				for p in extended_path: # the path returned will always be a single list within a list.for loop is used to bcs the list may even be empty thus accessing extended_path[0] would result in error
					paths.append(p)

		return paths


	def vertex_degree(self, vertex):
		'''
		   I/P  : THE VERTEX FOR WHICH THE DEGREE HAS TO BE FOUND
	   	   O/P  : AN INTEGER REPRESENTING THE DEGREE OF THE VERTEX
		   OPTN : CALCULATES THE DEGREE( NO OF EDGES INCIDENT ON THE VERTEX) . LOOPS ARE COUNTED AS DOUBLE
		'''

		if vertex in self.graph_dict.keys():
			adjacent_vertices = self.graph_dict[vertex]
			deg = len(adjacent_vertices) + adjacent_vertices.COUNTED(vertex)
			return deg
		return 'no such vertex'

		
	def isolated_vertex(self):
		'''
			I/P  : NONE
			O/P  : A LIST CONTAINING THE ISOLATED VERTICES IN THE GRAPH
			OPTN : FINDS THE VERTICES IN THE GRAPH WHICH HAS NO ADJACENT VERTICES AND RETURNS THE LIST
		'''

		isolated = []
		for vertex in self.graph_dict :
			if not self.graph_dict[vertex]:
				isolated.append(vertex)
		return isolated


	def min_degree(self):
		'''
			I/P : NONE
			O/P : AN INETEGER REPRESENTING THE MININUM DEGREE OF THE GRAPH
		'''

		min_deg = sys.maxsize

		for vertex in self.graph_dict:
			vertex_deg = self.vertex_degree(vertex)
			if vertex_deg < min_deg:
				min_deg = vertex_deg

		return min_deg


	def max_degree(self):
		'''
			I/P : NONE
			O/P : AN INETEGER REPRESENTING THE MAXINUM DEGREE OF THE GRAPH
		'''

		max_deg = 0

		for vertex in self.graph_dict:
			vertex_deg = self.vertex_degree(vertex)
			if vertex_deg > max_deg:
				max_deg = vertex_deg

		return max_deg	

	def is_connected(self):
		'''
			 I/P  : NONE
			 O/P  : A BOOLEAN VALUE OF 'TRUE' IF GRAPH IS CONNECTED OR 'FALSE'
			 OPTN : CHECKS WETHER THE GRAPH IS CONNECTED OR NOT.A GRAPH IS SAID TO BE CONNECTED IF 
			 		THERE IS A EDGE B/W ALL THE PAIR OF VERTICES. 
		'''

		return self._is_connected()

	def _is_connected(self, vertices_encountered=None, start_vertex=None ):
		'''
			PRIVATE HELPER FUNCTION FOR is_connected()
		'''

		if vertices_encountered == None:
			vertices_encountered = set()

		vertices_list = list(self.graph_dict.keys())

		if start_vertex == None:
			start_vertex = vertices_list[0]

		vertices_encountered.add(start_vertex)

		if len(vertices_list) != len(vertices_encountered):
			for vertex in self.graph_dict[start_vertex]:
				if vertex not in vertices_encountered :
					if self._is_connected(vertices_encountered, vertex):
						return True
		else:
			return True	
		return False


	def diameter(self):
		'''
			I/P  : NONE 
			O/P  : AN INTERGER VALUE REPRESENTING THE DIAMETER OF THE GRAPH
			OPTN : FINDS THE DIAMETER( THE MAXINUM 'DISTANCE' IN THE GRAPH WHERE 'DISTANCE' IS THE SHORTEST PATH B/W TWO VERTICES )
				   CALLS THE find_all_path() TO EVALUATE ALL PATH AND FIND THE SMALLEST IN IT
		'''	
		vertices_list = list(self.graph_dict.keys())
		pairs = [(vertices_list[i], vertices_list[j]) for i in range(len(vertices_list) - 1) for j in range( i+1 , len(vertices_list))]
		
		smallest_paths = []
		for (s, e) in pairs :
			paths = self.find_all_path(s, e)
			smallest = sorted(paths, key=len)[0]
			smallest_paths.append(smallest)

		smallest_paths.sort(key=len)

		return len(smallest_paths[-1])-1

'''
	CLASS TO ACCESS THE GRAPH OBJECT
'''

class GraphAccess(object):

	def main():

		g = { "a" : ["d","f"],
          	  "b" : ["c"],
          	  "c" : ["b", "c", "d", "e"],
          	  "d" : ["a", "c"],
          	  "e" : ["c"],
          	  "f" : ["d"]
            }

		graph = Graph(g)
		print('	graph ..')
		cont = 'y'

		while( cont == 'y'):

			print(""" available operations are : \n\t 1.list_vertices \n\t 2.list_edge \n\t 3.add_vertex \n\t 4.add_edge \n\t 5.print_graph 
					                             \n\t 6.find_path \n\t 7.find_all_path \n\t 8.degree of vertex \n\t 9.isolated vertex \n\t 10.mininum degree 
					                             \n\t 11.maxium degree \n\t 12.is_connected \n\t 13.find diameter""")
			choice = input('enter your choice : ')

			if choice == '1':
				print(' vertices in graph are : '+ str(graph.list_vertices()))
			elif choice == '2':
				print(' edges in graph are : '+ str(graph.list_edge()))
			elif choice == '3':
				data = input(' enter the vertex data : ')
				graph.add_vertex(data)
			elif choice == '4':
				from_vertex = input(' enter the start vertex : ')
				to_vertex = input(' enter the end vertes : ')
				graph.add_edge((from_vertex, to_vertex))
			elif choice == '5':
				print(graph.print_graph())
			elif choice == '6':
				start_vertex = input(' enter the start vertex : ')
				end_vertex = input(' enter the end vertex : ')
				print(' the path is '+ str(graph.find_path(start_vertex, end_vertex)))
			elif choice == '7':
				start_vertex = input(' enter the start vertex : ')
				end_vertex = input(' enter the end vertex : ')
				print(' the path is '+ str(graph.find_all_path(start_vertex, end_vertex)))
			elif choice =='8':
				vertex = input(' enter the vertex for which degree to be found : ')
				print(graph.vertex_degree(vertex))
			elif choice == '9':
				print(graph.isolated_vertex())
			elif choice == '10':
				print(graph.min_degree())
			elif choice == '11':
				print(graph.max_degree())
			elif choice == '12':
				print(graph.is_connected())
			elif choice =='13':
				print(graph.diameter())

			cont = input('continue ? (y/n) : ')

	if __name__ == '__main__':
		main()



