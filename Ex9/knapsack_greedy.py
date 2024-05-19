from collections import namedtuple

Item = namedtuple('Item', ['name', 'value', 'weight'])

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
    max_weight = float(input("Enter max weight knapsack can carry: "))
    items_str = input("Enter a list of items as <value,weight> tuples: ")
    items = [Item(i+1, float(item_str.split(",")[0]), float(item_str.split(",")[1])) for i, item_str in enumerate(items_str.split())]
    total_value, items_in_knapsack = knapsack_greedy(max_weight, items)
    print(f"Total Value: {total_value}")
    print(f"Items in knapsack: {items_in_knapsack}")

