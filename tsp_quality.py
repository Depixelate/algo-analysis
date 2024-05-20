import math
def nearest_neighbor(graph):
    visited = [False for i in range(len(graph))]
	cur_vert = 0
	dist = 0
	num_visited = 1
    visited[cur_vert] = True
	while num_visited != len(graph):
	    min_weight = math.inf
	    min_vert = -1
	    for i, weight in graph[cur_vert]:
	        if visited[i]:
	            continue
	        if weight < min_weight:
                min_weight = weight
                min_vert = i
    	num_visited += 1
        visited[cur_vert] = True
        dist += min_weight
        cur_vert = min_vert
    dist += graph[cur_vert][0]
    return dist
    
def get_mins(weights):
    m1 = m2 = math.inf
    for weight in weights:
        if weight < m1:
            m2 = m1
            m1 = weight
        elif weight < m2:
            m2 = weight
    return m1, m2

min_dist = math.inf
def bnb_best_first(graph, lb, cur_dist, edge_min, visited, cur_node):
    global min_dist
    for 

def bnb_best_first(graph):
    edge_min = []
    for i in range(len(graph)):
        graph[i].sort(key=lambda p:p[1])
        edge_min.append((graph[0] + graph[1])/2)
    
    
    
    
		
