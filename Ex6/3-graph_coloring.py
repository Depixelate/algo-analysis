# def color_graph(graph, num_colors, node_colors:dict[int,int]):
#     fully_colored = True

#     for i in range(len(graph)):
#         if i not in node_colors:
#             fully_colored = False
#             remaining_colors = set(range(num_colors))
#             neighbor_colors = {node_colors[j] for j in range(len(graph)) if graph[i][j] == 1 and j in node_colors}
#             remaining_colors.difference_update(neighbor_colors)

#             for color in remaining_colors:
#                 node_colors[i] = color
#                 result = color_graph(graph, num_colors, node_colors)

#                 if result:
#                     return True

#                 node_colors.pop(i)

#     return fully_colored

def color_graph(graph, num_colors, node_colors: dict[int,int], cur_node):
    if len(node_colors) == len(graph):
        return True

    remaining_colors = set(range(num_colors))

    for i, is_connected in enumerate(graph[cur_node]):
        if i in node_colors and is_connected == 1:
            remaining_colors.discard(node_colors[i])

    for color in remaining_colors:
        node_colors[cur_node] = color
        if color_graph(graph, num_colors, node_colors, cur_node + 1):
            return True
        node_colors.pop(cur_node)

    return False




num_nodes = int(input("Enter the number of nodes in the graph: "))
graph = []
for i in range(num_nodes):
    neighbors = [int(node) for node in input(f"Enter the nodes connected to node {i}: ").split(',')]
    row = [0] * num_nodes
    for neighbor in neighbors:
        row[neighbor] = 1
    graph.append(row)

num_colors = int(input("Enter the number of colors: "))

node_colors = {}
result = color_graph(graph, num_colors, node_colors, 0)
if result:
    print(f"Graph coloring: {node_colors}")
else:
    print("Coloring not possible!")
