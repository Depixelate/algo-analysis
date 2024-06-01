import math
from dataclasses import dataclass
import heapq
import random
import numpy as np
from collections import deque
import matplotlib.pyplot as plt
from datetime import datetime
import time

def nearest_neighbor(graph):
    visited = [False for i in range(len(graph))]
    cur_vert = 0
    dist = 0
    num_visited = 1
    visited[cur_vert] = True
    while num_visited != len(graph):
        #print(cur_vert, end = " ")
        min_weight = math.inf
        min_vert = -1
        for i, weight in graph[cur_vert]:
            if visited[i]:
                continue
            if weight < min_weight:
                min_weight = weight
                min_vert = i
        num_visited += 1
        visited[min_vert] = True
        dist += min_weight
        cur_vert = min_vert
    #print(cur_vert)
    dist += graph[cur_vert][0][1]
    return dist
    
def get_smallest_two(elems, key = lambda x:x):
    m1 = m2 = None
    for elem in elems:
        if m1 is None or key(elem) < key(m1):
            m2 = m1
            m1 = elem
        elif m2 is None or key(elem) < key(m2):
            m2 = elem
    return m1, m2

@dataclass(order=True)
class State:
    lower_bound: int
    cur_node: int
    visited: list[bool]
    num_visited: int
    partial_tour_length: int
    smallest_two_remaining: int
    
def calc_replacement(smallest_two_edges, w):
    cur_rep, next_rep = (smallest_two_edges[0], smallest_two_edges[1]) if w == smallest_two_edges[0] else (smallest_two_edges[1], smallest_two_edges[0])
    return cur_rep, next_rep    
    
def bnb_best_first(graph):
    if len(graph) <= 1:
        return 0
    if len(graph) == 2:
        return graph[0][1][1] * 2
    min_tour_length = math.inf
    verts_smallest_two_edges = [[] for i in range(len(graph))]
    lb = 0
    for i in range(len(graph)):
        v1, v2 = get_smallest_two(graph[i], key=lambda x: x[1] if x[0] != i else math.inf)
        lb += (v1[1] + v2[1])/2
        verts_smallest_two_edges[i].extend([v1[1], v2[1]])
    
        
    initial_state = State(visited=[False for i in range(len(graph))], num_visited=1, partial_tour_length=0, lower_bound=lb, cur_node=0, smallest_two_remaining=None)
    initial_state.visited[0] = True
    states = [initial_state]
    while len(states) > 0:
        state = heapq.heappop(states)
        # print(f"{state.lower_bound=}")
        
        if state.lower_bound >= min_tour_length:
            continue
        
        if state.num_visited >= len(graph) - 1:
            last_node = state.visited.index(False)
            tour_length = state.partial_tour_length + graph[state.cur_node][last_node][1] + graph[last_node][0][1]
            if tour_length < min_tour_length:
                min_tour_length = tour_length
            continue
            
        for v,w in graph[state.cur_node]:
            if state.visited[v]:
                continue
            if v == 2 and not state.visited[1]:
                continue
            replacement_edge1 = state.smallest_two_remaining if state.smallest_two_remaining is not None else calc_replacement(verts_smallest_two_edges[state.cur_node], w)[0]
            
        # nlb = state.lower_bound -  if state.rem is not None else state.lower_bound
            v_smallest_two_edges = verts_smallest_two_edges[v]
            replacement_edge2, next_replacement = calc_replacement(v_smallest_two_edges, w)
            nlb = state.lower_bound
            nlb -= (replacement_edge1 + replacement_edge2)/2
            nlb += w
            if nlb >= min_tour_length:
                continue
            new_state = State(lower_bound = nlb, cur_node=v, visited=list(state.visited), num_visited=state.num_visited+1, partial_tour_length=state.partial_tour_length + w, smallest_two_remaining=next_replacement)
            new_state.visited[v]=True
            heapq.heappush(states, new_state)
    return min_tour_length

def bnb_breadth_first(graph):
    if len(graph) <= 1:
        return 0
    if len(graph) == 2:
        return graph[0][1][1] * 2
    min_tour_length = math.inf
    verts_smallest_two_edges = [[] for i in range(len(graph))]
    lb = 0
    for i in range(len(graph)):
        v1, v2 = get_smallest_two(graph[i], key=lambda x: x[1] if x[0] != i else math.inf)
        lb += (v1[1] + v2[1])/2
        verts_smallest_two_edges[i].extend([v1[1], v2[1]])
    
        
    initial_state = State(visited=[False for i in range(len(graph))], num_visited=1, partial_tour_length=0, lower_bound=lb, cur_node=0, smallest_two_remaining=None)
    initial_state.visited[0] = True
    states = deque([initial_state])
    while len(states) > 0:
        state = states.popleft()
        # print(f"{state.lower_bound=}")
        
        if state.lower_bound >= min_tour_length:
            continue
        
        if state.num_visited >= len(graph) - 1:
            last_node = state.visited.index(False)
            tour_length = state.partial_tour_length + graph[state.cur_node][last_node][1] + graph[last_node][0][1]
            if tour_length < min_tour_length:
                min_tour_length = tour_length
            continue
            
        for v,w in graph[state.cur_node]:
            if state.visited[v]:
                continue
            if v == 2 and not state.visited[1]:
                continue
            replacement_edge1 = state.smallest_two_remaining if state.smallest_two_remaining is not None else calc_replacement(verts_smallest_two_edges[state.cur_node], w)[0]
            
        # nlb = state.lower_bound -  if state.rem is not None else state.lower_bound
            v_smallest_two_edges = verts_smallest_two_edges[v]
            replacement_edge2, next_replacement = calc_replacement(v_smallest_two_edges, w)
            nlb = state.lower_bound
            nlb -= (replacement_edge1 + replacement_edge2)/2
            nlb += w
            if nlb >= min_tour_length:
                continue
            new_state = State(lower_bound = nlb, cur_node=v, visited=list(state.visited), num_visited=state.num_visited+1, partial_tour_length=state.partial_tour_length + w, smallest_two_remaining=next_replacement)
            new_state.visited[v]=True
            states.append(new_state)
    return min_tour_length

def prim(graph):
    tree = [[] for i in range(len(graph))]
    visited = [False for i in range(len(graph))]
    visited[0] = True
    edge_heap = [(weight, 0, end) for end, weight in graph[0] if not visited[end]]
    heapq.heapify(edge_heap)
    while len(edge_heap) > 0:
        weight, start, end = heapq.heappop(edge_heap)
        if visited[end]:
            continue
        tree[start].append((end, weight))
        visited[end] = True
        for v, w in graph[end]:
            if visited[v]:
                continue
            heapq.heappush(edge_heap, (w, end, v))
    return tree
    
def preorder(graph, node):
    #print(node, end = " ")
    for v, _ in graph[node]:
        preorder(graph, v)

def mst_tour(graph):
    tree = prim(graph)
    dist = 0
    stack = deque([0])
    prev = None
    while len(stack) > 0:
        node = stack.pop()
        if prev is not None:
            dist += graph[prev][node][1]
        for i in range(len(tree[node]) - 1, -1, -1):
            stack.append(tree[node][i][0])
        prev = node
    
    dist += graph[prev][0][1]
    return dist

def div(a, b):
    if b == 0 and a != 0:
        return math.inf
    if a == 0 and b == 0:
        return 1
    return a/b
        
def test_quality():
    n = 10
    mst_quality = []
    nearest_neighbor_quality = []
    #capacities = [50]
    nums_locations = list(range(1, n+1))
    for num_locations in nums_locations:
        rep = 50
        mst_quality_sum = 0
        nearest_neighbor_quality_sum = 0
        for i in range(rep):
            adj_lst = [[None for k in range(num_locations)] for j in range(num_locations)]
            height = 20
            width = 20
            points = [(random.random() * width, random.random() * height) for _ in range(num_locations)]        
            
            for j in range(len(adj_lst)):
                for k in range(len(adj_lst)):
                    adj_lst[j][k] = k, ((points[j][0] - points[k][0])**2 + (points[j][1] - points[k][1])**2)**0.5
            
            tour_length_mst = mst_tour(adj_lst)
            tour_length_nn = nearest_neighbor(adj_lst)
            tour_length_best_first = bnb_best_first(adj_lst)
            #print(value_dpp, value_greedy)
            
            mst_quality_sum += div(tour_length_mst,tour_length_best_first)
            nearest_neighbor_quality_sum += div(tour_length_nn,tour_length_best_first)
        mst_quality.append(mst_quality_sum/rep)
        nearest_neighbor_quality.append(nearest_neighbor_quality_sum/rep)
        
    plt.plot(nums_locations, mst_quality, label='MST Tour')
    plt.plot(nums_locations, nearest_neighbor_quality, label='Nearest Neighbor')
    plt.legend()
    plt.ylabel('Accuracy Ratio')
    plt.xlabel('Number of Locations') 
    plt.savefig(f"tsp_quality-{int(datetime.now().timestamp())}.png")
    
def test_speed():
    n = 20
    names = {'mst': 'MST Tour', 'nn': 'Nearest Neighbor', 'bnb_best': 'Branch and Bound, Best First', 'bnb_breadth': 'Branch and Bound, Breadth First'}
    speeds = {'mst': [], 'nn': [], 'bnb_best': [], 'bnb_breadth': []}
    funcs = {'mst': mst_tour, 'nn': nearest_neighbor, 'bnb_best': bnb_best_first, 'bnb_breadth': bnb_breadth_first}
    
    #capacities = [50]
    nums_locations = list(range(1, n+1))
    for num_locations in nums_locations:
        rep = 2
        speed_sums = {'mst': 0, 'nn': 0, 'bnb_best': 0, 'bnb_breadth': 0}
        for i in range(rep):
            adj_lst = [[None for k in range(num_locations)] for j in range(num_locations)]
            height = 20
            width = 20
            points = [(random.random() * width, random.random() * height) for _ in range(num_locations)]        
            
            for j in range(len(adj_lst)):
                for k in range(len(adj_lst)):
                    adj_lst[j][k] = k, ((points[j][0] - points[k][0])**2 + (points[j][1] - points[k][1])**2)**0.5
                    
            for algo in funcs:
                start = time.perf_counter()
                funcs[algo](adj_lst)
                end = time.perf_counter()
                speed_sums[algo] += end - start
            
            #print(value_dpp, value_greedy)
        for algo in speeds:
            speeds[algo].append(speed_sums[algo]/rep)
    
    for algo in speeds:
        plt.plot(nums_locations, speeds[algo], label=names[algo])
    plt.legend()
    plt.ylabel('Time(s)')
    plt.xlabel('Number of Locations') 
    plt.yscale("log")
    plt.xscale("log")
    plt.savefig(f"tsp_speed-{int(datetime.now().timestamp())}.png")

def main():
    n = 10
    adj_lst = [[None for j in range(n)] for i in range(n)]
    
    height = 20
    width = 20
    points = [(random.random() * width, random.random() * height) for _ in range(n)]
    
    for i in range(len(adj_lst)):
        for j in range(len(adj_lst)):
            adj_lst[i][j] = j, ((points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2)**0.5
                    
    # for row in adj_lst:                     
    #     print(row)
    
    #adj_mat = [[adj_lst[i][j][1] for j in range(n)] for i in range(n)]
    
    print(f"{nearest_neighbor(adj_lst)=}")
    print(f"{mst_tour(adj_lst)=}")
    print(f"{bnb_best_first(adj_lst)=}")
    print(f"{bnb_breadth_first(adj_lst)=}")
    #print(f"{solve_tsp_dynamic_programming(np.array(adj_mat))}")
    plt.scatter(*zip(*points))
    for i, point in enumerate(points):
        plt.text(point[0], point[1], str(i))
    plt.show()

if __name__ == "__main__":
    test_speed()
    
    
    
    
    
        
