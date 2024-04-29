import math
import numpy as np

def floyd_warshall(graph):
    D = [[graph[i][j] for j in range(len(graph))] for i in range(len(graph))]
    N = [[j for j in range(len(graph))] for i in range(len(graph))]
    for k in range(len(graph)):
        for i in range(len(graph)):
            for j in range(len(graph)):
                if D[i][k] + D[k][j] < D[i][j]:
                    D[i][j] = D[i][k] + D[k][j]
                    N[i][j] = N[i][k]
    return D, N

def print_path(graph, D, N, i, j):
    print(i, end="")
    cur = i
    while(cur != j):
        next = N[cur][j]
        print(f"-[{graph[cur][next]}]->{next}", end="")
        cur = next
    print()
    print(f"Total Distance: {D[i][j]}")

        
if __name__ == "__main__":
    num_nodes = int(input("Enter the number of nodes in the graph: "))
    graph = []
    for i in range(num_nodes):
        neighbors = [(int(node.split(',')[0]), float(node.split(',')[1])) for node in input(f"Enter the node,weight connected to node {i}: ").split(' ')]
        row = [math.inf] * num_nodes
        row[i] = 0
        for neighbor, weight in neighbors:
            row[neighbor] = weight
        graph.append(row)
    D, N = floyd_warshall(graph)
    
    print("Shortest Path Lengths: ")

    for row in D:
        print(row)
    
    while(True):
        start, end = [int(node) for node in input("Enter start,end nodes: ").split(',')]
        print_path(graph, D, N, start, end)
    
