import math
def change_dp_helper(table, coins, amount, cur_coin):
    if amount == 0:
        return 0
    
    if cur_coin >= len(coins):
        return math.inf
    
    if table[cur_coin][amount] is None:
        min_coins = math.inf
        min_i = -1
        min_coins_remaining_amount = None
        for i in range(amount // coins[cur_coin] + 1):
            remaining_amount = amount - i * coins[cur_coin]
            num_coins = change_dp_helper(table, coins, remaining_amount, cur_coin + 1) + i
            if num_coins < min_coins:
                min_coins = num_coins
                min_i = i
                min_coins_remaining_amount = remaining_amount
        table[cur_coin][amount] = min_coins, min_i, min_coins_remaining_amount
  
    return table[cur_coin][amount][0]

def change_dp(coins, amount):
    table = [[None for j in range(amount+1)] for i in range(len(coins))]
    num_coins = change_dp_helper(table, coins, amount, 0)
    if num_coins == math.inf:
        return num_coins, None
    coins = get_coins(table, amount)
    return num_coins, coins

def get_coins(table, amount):
    coins = []
    cur_coin = 0
    while amount != 0:
        coins.append(table[cur_coin][amount][1])
        amount = table[cur_coin][amount][2]
        cur_coin += 1
    return coins

def main():
    denoms = list(eval(input("Enter a comma-separated list of coin denominations: ")))
    target = int(input("Enter the target amount to make change for: "))
    min_coins, min_change = change_dp(denoms, target)
    print(f"Minimum number of coins required to make change: {min_coins}")
    print(f"Change: {min_change}")


if __name__ == "__main__":
    main()
    
    
    