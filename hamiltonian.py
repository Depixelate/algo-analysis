def hamiltonian_path(graph, path = None, visited = None):
    n = len(graph)
    if path is None:
        path = [0]
        visited = [False for i in range(n)]
        visited[0] = True
    
    cur = path[-1]
    
    if len(path) == n:
        if 0 in graph[cur]:
            print(path)
        return
        
    
    for v in graph[cur]:
        if visited[v]:
            continue
        path.append(v)
        visited[v] = True
        hamiltonian_path(graph, path, visited)
        visited[v] = False
        path.pop()
    
graph = [
    [1, 2, 3],
    [0, 2, 5],
    [0, 1, 3, 4],
    [0, 2, 4],
    [2, 3, 5],
    [1, 4]
]

hamiltonian_path(graph)


def merge_sort_inversions(array, start=0, end=None):
    if end is None:
        end = len(array) - 1
    if end <= start:
        return 0
    s1 = start
    e1 = (start + end)//2
    s2 = (start + end) // 2 + 1
    e2 = end
    inv = merge_sort_inversions(array, s1, e1)
    inv += merge_sort_inversions(array, s2, e2)
    
    temp = [0 for i in range(end - start + 1)]
    
    for i in range(end - start + 1):
        if s1 > e1:
            temp[i] = array[s2]
            s2 += 1
            continue
        if s2 > e2:
            temp[i] = array[s1]
            s1 += 1
            continue
        if array[s1] <= array[s2]:
            temp[i] = array[s1]
            s1 += 1
        else:
            temp[i] = array[s2]
            s2 += 1
            inv += e1 - s1 + 1
    for i in range(end - start + 1):
        array[start + i] = temp[i]
    
    return inv

print(merge_sort_inversions(list(range(101, 0, -1))))
    

    
    
    
    