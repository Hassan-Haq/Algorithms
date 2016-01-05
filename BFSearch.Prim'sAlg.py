import random
import Queue

#Hassan Haq
#Student ID: 10061306



'''
Part 1: Breadth First Search
'''
def BFS(g):
        #sum of the path
	total = 0

	vertices = list(range(len(g))) # list from 0 -> n-1
	start = random.choice(vertices) #can start at any vertex in the graph
	visited = [False] * len(g) # mark visited vertcies

	Q = Queue.Queue()
	Q.put(start)
	visited[start] = True

	while not Q.empty():
		vertex = Q.get()
		siblings = findSiblings(g, vertex) #find the relatives of vertex
		for i in siblings:
			if not visited[i]: #if a vertex isn't visited then work on it
				total += g[vertex][i]
				visited[i] = True # mark visited and add to queue
				Q.put(i)

	return total

'''
Part 2: Prim's Minimum Spanning Tree
        Prim's algorithm to transform a graph into a minimum spanning tree
        

'''
def primsMST(graph):
	size = len(graph)
	total = 0

	vertices = [0] * size
	weights = [float("inf")] * size
	inTree = [False] * size

	inTree[0] = True
	bestSibling = 0

	for i in range(size - 1):
		
		minWeight = float("inf")

		for j in range(size):
			if not inTree[j]:
				weight = graph[bestSibling][j]
				if weight != 0 and weight < weights[j]:
					vertices[j] = bestSibling
					weights[j] = weight

		for j in range(size):
			if not inTree[j]:
				if weights[j] < minWeight:
					bestSibling = j
					minWeight = weights[j]

		if bestSibling != 0:
			total += weights[bestSibling]
			inTree[bestSibling] = True

	return total

'''
Helper Function that takes a graph and a vertex and returns all the siblings of that vertex
'''
def findSiblings(graph, vertex):
	siblings = []
	for i in range(len(graph)):
		if graph[vertex][i] != 0:
			siblings.append(i)
	return siblings
'''
Part 3: Random Graph Generator
        Takes a number for the number of vertecies and generates a graph it with randomly weighted edges
'''
def randomGraph(n):
	
	# creates an empty matrix
	matrix = []
	for i in range(n):
		matrix.append([0] * n)

	v = list(range(n))

	for i in range(1, n):
		sampleS = random.randint(1, i)
		random.shuffle(v)
		sample = v[0:sampleS]

		# assigning the weights
		for vertex in sample:
			w = random.randint(10, 100)
			#assigning the weight to both ends of the edge
			matrix[i][vertex] = w
			matrix[vertex][i] = w
        #Return the Matrix for the random Graph
	return matrix
'''
Part 3: Final tests
        Using the random graph generator we test the effeciency of the BFS Algorithm (Part 1) and Prim's Algorithm (Part 2) Using n values of: 100, 200, 300, 400 & 500
'''
def test ():
        randGraphs = [2000]
        for j in randGraphs:
                print("Test n = %d" %j)
                total = 0
                for i in range(1,10):
                        #Calls to Random Graph, BFS and MST algorightms
                        graph = randomGraph(j)
                        bfs = BFS(graph)
                        pMST = primsMST(graph)
                        #Calculating the ratio for each run of the function and adding the total
                        ratio = pMST/(float)(bfs)
                        total = total + ratio
                #Taking the average of each n value using the total of the ratios.
                average = total/10
                print ("average ratio: %f" %average)
                

def main():
	testMat = [[0, 15, 0, 7, 10, 0], [15, 0, 9, 11, 0, 9], [0, 9, 0, 0, 12, 7], [7, 11, 0, 0, 8, 14], [10, 0, 12, 8, 0, 8], [0, 9, 7, 14, 8, 0]]
	print("Sum Path for BFS: %d" %BFS(testMat))
	print("MST Total for Prim's: %d" %primsMST(testMat))
	test()

main()
