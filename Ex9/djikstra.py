import heapq
import math


def djikstra(adjacency_list, start):
    nodes = [(0, start)]
    prev = {start: start}
    dist = {start: 0}
    done = set()
    while len(nodes) != 0:
        _, node = heapq.heappop(nodes)
        if node in done:
            continue
        for other, weight in adjacency_list[node]:
            if other in done:
                continue
            
            if weight + dist[node] < dist.get(other, math.inf):
                dist[other] = weight + dist[node]
                prev[other] = node
                heapq.heappush(nodes, (dist[other], other))    

        done.add(node)

    return dist, prev

def djikstra_2(adjacency_list, start):
    n = len(adjacency_list)
    prevs = [i for i in range(n)]
    dists = [math.inf for i in range(n)]
    visited = [False for i in range(n)]
    
    verts = [(0, start, start)]
    while len(verts) > 0:
        dist, vert, prev = heapq.heappop(verts)
        if visited[vert]:
            continue
        visited[vert] = True
        prevs[vert] = prev
        dists[vert] = dist
        for v, w in adjacency_list[vert]:
            if visited[v]:
                continue
            heapq.heappush(verts, (w + dist, v, vert))
    return dists, prevs

def print_path_h(dist, prev, node):
    if prev[node] == node:
        print(node, end="")
        return
    print_path_h(dist, prev, prev[node])
    print(f"->{node}", end="")


def print_path(dist, prev, node):
    print_path_h(dist, prev, node)
    print()


if __name__ == "__main__":
    num_nodes = int(input("Enter the number of nodes in the graph: "))
    adj_lst = []
    for i in range(num_nodes):
        neighbors = [
            (int(node.split(",")[0]), float(node.split(",")[1]))
            for node in input(f"Enter the node,weight connected to node {i}: ").split(
                " "
            )
        ]
        adj_lst.append(neighbors)
    start = int(input("Enter the starting node: "))
    print("Adjacency list: ")
    print(adj_lst)
    dist, prev = djikstra_2(adj_lst, start)
    print(f"Shortest Path Lengths: {dist}")
    print(prev)
    while True:
        end = int(input("Enter an ending node: "))
        print("Path: ")
        print_path(dist, prev, end)
