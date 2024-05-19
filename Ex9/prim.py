import heapq


def edges_to_adjlst(num_nodes, edges):
    adj_lst = [[] for i in range(num_nodes)]
    for weight, start, end in edges:
        adj_lst[start].append((end, weight))
    return adj_lst


def prim(adj_lst, start=0):
    min_span_tree = []
    visited = [False for i in range(len(adj_lst))]
    visited[start] = True
    edge_heap = [(weight, start, node) for node, weight in adj_lst[start]]
    heapq.heapify(edge_heap)
    while edge_heap:
        weight, s_node, e_node = heapq.heappop(edge_heap)
        if visited[e_node]:
            continue
        min_span_tree.append((weight, s_node, e_node))
        for node, weight in adj_lst[e_node]:
            if not visited[node]:
                heapq.heappush(edge_heap, (weight, e_node, node))
        visited[e_node] = True
    return edges_to_adjlst(len(adj_lst), min_span_tree)


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
    print("Adjacency List: ")
    print(adj_lst)
    print("Minimum Spanning Tree:")
    print(prim(adj_lst))
