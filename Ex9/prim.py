import math
import heapq

def prim(adj_lst, start = 0):
	min_span_tree = []
	visited = [False for i in range(len(adj_lst))]	
	visited[start] = True
	edge_heap = [(weight, start, node) for node, weight in adj_lst[start]]
	heapq.heapify(edge_heap)
	while edge_heap:
		weight, s_node, e_node = heapq.pop(edge_heap)
		if visited[e_node]:
			continue
		min_span_tree.append((weight, s_node, e_node))
		for node, weight in adj_lst[e_node]:
			if node not in visited:
				heqpq.push(edge_heap, (weight, e_node, node))
		visited[e_node] = True;
	return min_span_tree
	
		
