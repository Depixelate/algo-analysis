def color_graph(graph, num_colors, node_colors:dict[int,int]):
    fully_colored = True

    for i in range(len(graph)):
        if i not in node_colors:
            fully_colored = False
            remaining_colors = set(range(num_colors))
            neighbor_colors = {node_colors[j] for j in range(len(graph)) if graph[i][j] == 1 and j in node_colors}
            remaining_colors.difference_update(neighbor_colors)

            for color in remaining_colors:
                node_colors[i] = color
                result = color_graph(graph, num_colors, node_colors)

                if result:
                    return True
                
                node_colors.pop(i)
    
    return fully_colored        


graph = [[0, 1, 1], [1, 0, 1], [1, 1, 0]]
node_colors = {}
result = color_graph(graph, 3, node_colors)
if result:
    print(f"Graph coloring: {node_colors}")
else:
    print("Coloring not possible!")
