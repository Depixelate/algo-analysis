class DSU:
    def __init__(self, num_sets):
        self.rep = [i for i in range(num_sets)]
        self.rank = [0 for i in range(num_sets)]

    def get_rep(self, elem):
        if elem != self.rep[elem]:
            self.rep[elem] = self.get_rep(self.rep[elem])
        return self.rep[elem]

    def union(self, i, j):
        rep_i, rep_j = self.get_rep(i), self.get_rep(j)
        if self.rank[rep_i] > self.rank[rep_j]:
            self.rep[rep_j] = rep_i
        else:
            self.rep[rep_i] = rep_j
            if self.rank[rep_i] == self.rank[rep_j]:
                self.rank[rep_j] += 1
        return self.rep[rep_i]

    def same_set(self, i, j):
        return self.get_rep(i) == self.get_rep(j)


def edges_to_adjlst(num_nodes, edges):
    adj_lst = [[] for i in range(num_nodes)]
    for weight, start, end in edges:
        adj_lst[start].append((end, weight))
    return adj_lst


def kruskal(adj_lst):
    min_span_tree = []
    forest = DSU(len(adj_lst))
    sorted_edges = [
        (weight, s, e) for s in range(len(adj_lst)) for e, weight in adj_lst[s]
    ]
    sorted_edges.sort()
    for edge in sorted_edges:
        _, start, end = edge
        if forest.same_set(start, end):
            continue
        min_span_tree.append(edge)
        forest.union(start, end)

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
    print(kruskal(adj_lst))
