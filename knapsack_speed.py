from collections import namedtuple
import random
import matplotlib.pyplot as plt
import time

Item = namedtuple("Item", ["name", "value", "weight"])
Entry = namedtuple("Entry", ["keep_item", "index", "value", "ref"])


def knapsack_dpp_helper(table, weight_left, items, index):
    if index >= len(items):
        return 0

    if (index, weight_left) in table:
        return table[(index, weight_left)].value 

    item_weight = items[index].weight
    keep_item = (
        (
            knapsack_dpp_helper(table, weight_left - item_weight, items, index + 1)
            + items[index].value,
            table.get((index + 1, weight_left - item_weight)),
        )
        if weight_left >= item_weight
        else (0, None)
    )
    skip_item = (knapsack_dpp_helper(table, weight_left, items, index + 1), table.get((index+1, weight_left)))
    item = max(keep_item, skip_item, key=lambda item:item[0])
    table[(index, weight_left)] = Entry(keep_item=item is keep_item, index=index, value=item[0], ref=item[1])
    return item[0]

def knapsack_dpp(max_weight, items):
    table = {}
    return knapsack_dpp_helper(table, max_weight, items, 0), table

def get_items(ref, items, knapsack_items):
    if ref is None:
        return
    if ref.keep_item:
        knapsack_items.append(items[ref.index])
    get_items(ref.ref, items, knapsack_items)
    
def knapsack_greedy(max_weight, items):
    items.sort(key=lambda item: item.value/item.weight, reverse=True)
    weight_left = max_weight
    total_value = 0
    items_in_knapsack = []
    for item in items:
        _, value, weight = item
        if weight <= weight_left:
            items_in_knapsack.append(item)
            weight_left -= weight
            total_value += value
    return total_value, items_in_knapsack


if __name__ == "__main__":
    n = 100
    greedy_time = []
    dp_time = []
    capacities = list(range(1, n+1))
    for capacity in capacities:
        rep = 25
        greedy_time_sum = 0
        dp_time_sum = 0
        for i in range(rep):
            num_items = random.randint(1, capacity)
            min_weight = 1
            max_weight = capacity
            min_value = 1
            max_value = capacity
            items = []
            for i in range(capacity):
                value = random.randint(min_value, max_value)
                weight = random.randint(min_weight, max_weight)
                items.append(Item(1, value, weight))
            
            start = time.process_time()
            value_dpp, _ = knapsack_dpp(capacity, items)
            end = time.process_time()
            dp_time_sum += end - start
            start = time.process_time()
            value_greedy, _ = knapsack_greedy(capacity, items)
            end = time.process_time()
            greedy_time_sum += end - start
        greedy_time.append(greedy_time_sum/5)
        dp_time.append(dp_time_sum/5)
        
    plt.plot(capacities, greedy_time,label='greedy')    
    plt.plot(capacities, dp_time,label='dp')  
    plt.legend()  
    plt.show()
        
        
    
