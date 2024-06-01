from collections import namedtuple
import random
import matplotlib.pyplot as plt
import time
from datetime import datetime

Item = namedtuple("Item", ["name", "value", "weight"])


def knapsack_dpp_helper(table, weight_left, items, index):
    if index >= len(items):
        return 0

    if (index, weight_left) in table:
        return table[(index, weight_left)] 

    item_weight = items[index].weight
    keep_value = knapsack_dpp_helper(table, weight_left - item_weight, items, index + 1) + items[index].value if weight_left >= item_weight else 0
    skip_value = knapsack_dpp_helper(table, weight_left, items, index + 1)
    max_value = max(keep_value, skip_value)
    table[(index, weight_left)] = max_value
    return max_value

def knapsack_dpp(max_weight, items):
    table = {}
    return knapsack_dpp_helper(table, max_weight, items, 0)

# def get_items(ref, items, knapsack_items):
#     if ref is None:
#         return
#     if ref.keep_item:
#         knapsack_items.append(items[ref.index])
#     get_items(ref.ref, items, knapsack_items)
    
def knapsack_greedy(max_weight, items):
    items.sort(key=lambda item: item.value/item.weight, reverse=True)
    weight_left = max_weight
    total_value = 0
    #items_in_knapsack = []
    for item in items:
        _, value, weight = item
        if weight <= weight_left:
            #items_in_knapsack.append(item)
            weight_left -= weight
            total_value += value
        
    return total_value

def test_quality():
    n = 100
    greedy_quality = []
    capacities = list(range(1, n+1))
    for capacity in capacities:
        rep = 1000
        greedy_quality_sum = 0
        for i in range(rep):
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
            
            value_dpp = knapsack_dpp(capacity, items)
            value_greedy = knapsack_greedy(capacity, items)
            greedy_quality_sum += value_dpp/value_greedy
        greedy_quality.append(greedy_quality_sum/rep)
        
    plt.plot(capacities, greedy_quality)
    plt.xlabel("Maximum Capacity and Number of Items")
    plt.ylabel("Greedy-To-DP Ratio")
    plt.savefig(f"0-1_knapsack_quality-{int(datetime.now().timestamp())}.png")    
        
def test_speed():
    n = 100
    greedy_time = []
    dp_time = []
    capacities = list(range(1, n+1))
    for capacity in capacities:
        rep = 25
        greedy_time_sum = 0
        dp_time_sum = 0
        for i in range(rep):
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
    # plt.yscale("log")
    # plt.xscale("log")
    plt.xlabel("Maximum Capacity and Number of Items")
    plt.ylabel("Time(s)")
    plt.savefig(f"0-1_knapsack_speed-{int(datetime.now().timestamp())}.png")
    

if __name__ == "__main__":
    test_quality()
    #test_speed()