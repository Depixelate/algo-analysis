def make_change_greedy(target, coins):
    change = {}
    coins.sort(reverse=True)
    remaining = target

    for coin in coins:
        change[coin] = remaining // coin
        remaining %= coin
    
    return change

def main():
    coins = [1, 5, 10, 25]
    target = int(input("Enter the target amount to make change for: "))
    change = make_change_greedy(target, coins)
    num_coins = sum(change.values())
    print(f"Minimum number of coins required to make change: {num_coins}")
    print(f"Change: {change}")

if __name__ == "__main__":
    main()
