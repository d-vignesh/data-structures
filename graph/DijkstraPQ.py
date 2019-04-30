
'''
	PROGRAM TO IMPLEMENT DIJKSTRA ALGO TO FIND SHORTEST PATH TO ALL VERTEX FROM A SOURCE VERTEX
'''

from collections import defaultdict
from heapq import *
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s -- %(levelname)s -- %(message)s')



def dijkstra( edges, f, t):
	logging.debug('start of dijkstra')
	
	g = defaultdict(list)
	for l,r,c in edges:
		g[l].append((c, r))

	logging.debug('The constructed graph is : ')
	logging.debug(g)

	q, seen, mins = [(0, f, ())], set(), {f:0}

	while(q):

		(cost, v1, path) = heappop(q)

		logging.debug(' current min vertex is : ' + v1)
		logging.debug(' the cost is : '+ str(cost))
		logging.debug(' the path is : '+ str(path))

		logging.debug(' vertices visited before adding : '+ str(seen))

		if v1 not in seen:
			seen.add(v1)
			path = (v1, path)
			if v1 == t : 
				return (cost, path)

			logging.debug(' vertex added to seen set : '+ str(seen))


			for c, v2 in g.get(v1, ()):
				logging.debug(' checking the adajcent vertices : '+ v2)
				if v2 in seen :
					continue

				logging.debug(f' trying to add the unvisited vertex :{v2} with the cost : {c}')
				prev = mins.get(v2, None)
				next = cost + c
				if prev is None or next < prev:
					mins[v2] = next
					heappush(q, (next, v2, path))
			

			logging.debug('the state of the mins dict : ')
			logging.debug(str(mins))	
			logging.debug('the state of the vertex queue : ')
			logging.debug(str(q))

			print('-' * 70)


	return float('inf')


if __name__ == "__main__":
    edges = [
        ("A", "B", 7),
        ("A", "D", 5),
        ("B", "C", 8),
        ("B", "D", 9),
        ("B", "E", 7),
        ("C", "E", 5),
        ("D", "E", 15),
        ("D", "F", 6),
        ("E", "F", 8),
        ("E", "G", 9),
        ("F", "G", 11)
    ]

    print("=== Dijkstra ===")
    print(edges)
    print("A -> E:")
    print(dijkstra(edges, "A", "E"))
    print("F -> G:")
    print(dijkstra(edges, "F", "G"))


