from collections import namedtuple

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



if __name__ == "__main__":
    max_weight = float(input("Enter max weight knapsack can carry: "))
    items_str = input("Enter a list of items as <value,weight> tuples: ")
    items = [
        Item(i + 1, float(item_str.split(",")[0]), float(item_str.split(",")[1]))
        for i, item_str in enumerate(items_str.split())
    ]
    total_value, table = knapsack_dpp(max_weight, items)
    print(f"Total Value: {total_value}")
    knapsack_items = []
    get_items(table.get((0, max_weight)), items, knapsack_items)
    print(f"Items in knapsack: {knapsack_items}")
