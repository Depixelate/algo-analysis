from collections import namedtuple
import random
import matplotlib.pyplot as plt
import time
from datetime import datetime
from matplotlib.ticker import ScalarFormatter

Item = namedtuple("Item", ["name", "value", "weight"])

def get_table_value(table, i, j):
    if i < 0:
        return 0
    if j < 0:
        return 0
    return table[i][j]

def knapsack_dpp(max_weight, items):
    items.sort(key=lambda item:item.value/item.weight)
    #print(items)
    table = [[0 for j in range(max_weight)] for i in range(len(items))]
    for i in range(len(items)):
        for j in range(max_weight):
            weight_left = j + 1
            cur_item = i
            weight_used = min(items[cur_item].weight, weight_left)
            value_gained = items[cur_item].value*weight_used/items[cur_item].weight
            new_weight_left = weight_left - weight_used
            new_j = new_weight_left - 1
            table[i][j] = value_gained + get_table_value(table, i-1, new_j)
    #print(table)
    return table[len(items)-1][max_weight-1]
    
def knapsack_greedy(max_weight, items):
    items.sort(key=lambda item: item.value/item.weight, reverse=True)
    weight_left = max_weight
    total_value = 0
    #items_in_knapsack = []
    for item in items:
        weight_used = min(item.weight, weight_left)
        value_gained = item.value*weight_used/item.weight
        weight_left -= weight_used
        total_value += value_gained
        if weight_left == 0:
            break
        
    return total_value

def test_quality():
    n = 100
    greedy_quality = []
    capacities = list(range(1, n+1))
    #capacities = [50]
    for capacity in capacities:
        rep = 25
        greedy_quality_sum = 0
        for i in range(rep):
            num_items = capacity
            #num_items = 5 
            min_weight = 1
            max_weight = capacity
            min_value = 1
            max_value = capacity
            items = []
            
            for i in range(num_items):
                value = random.randint(min_value, max_value)
                weight = random.randint(min_weight, max_weight)
                items.append(Item(1, value, weight))
            
            value_dpp = knapsack_dpp(capacity, items)
            value_greedy = knapsack_greedy(capacity, items)
            #print(value_dpp, value_greedy)
            greedy_quality_sum += value_dpp/value_greedy
        greedy_quality.append(greedy_quality_sum/rep)
        
    plt.plot(capacities, greedy_quality)
    plt.ylabel('Greedy-to-DP Ratio')
    plt.xlabel('Maximum Capacity and Number of Items') 
    plt.savefig(f"continuous_knapsack_quality-{int(datetime.now().timestamp())}.png")
        
def test_speed():
    n = 100
    greedy_time = []
    dp_time = []
    capacities = list(range(1, n+1))
    for capacity in capacities:
        rep = 100
        greedy_time_sum = 0
        dp_time_sum = 0
        for i in range(rep):
            #num_items = random.randint(1, capacity)
            num_items = capacity
            min_weight = 1
            max_weight = capacity
            min_value = 1
            max_value = capacity
            items = []
            for i in range(num_items):
                value = random.randint(min_value, max_value)
                weight = random.randint(min_weight, max_weight)
                items.append(Item(1, value, weight))
            
            start = time.perf_counter()
            knapsack_dpp(capacity, items)
            end = time.perf_counter()
            dp_time_sum += end - start
            start = time.perf_counter()
            knapsack_greedy(capacity, items)
            end = time.perf_counter()
            greedy_time_sum += end - start
        greedy_time.append(greedy_time_sum/rep)
        dp_time.append(dp_time_sum/rep)
        
    plt.plot(capacities, greedy_time,label='greedy')    
    plt.plot(capacities, dp_time,label='dp')  
    plt.legend()  
    plt.yscale("log")
    plt.xscale("log")
    plt.xlabel("Maximum Capacity and Number of Items")
    plt.ylabel("Time(s)")
    # scalar_format = ScalarFormatter()
    # scalar_format.set_scientific(False)
    # fig, ax = plt.subplots()
    # ax.xaxis.set_major_formatter(scalar_format)
    plt.savefig(f"continuous_knapsack_speed-{int(datetime.now().timestamp())}.png")         

if __name__ == "__main__":
    #test_quality()
    test_quality()