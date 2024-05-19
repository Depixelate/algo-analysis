import math

min_coins = math.inf
min_change = None
def make_change_bnb_helper(change, target_remaining, denoms, index, coins_used):
    global min_coins
    global min_change

    print(f"{change=}, {target_remaining=}, {index=}, {min_coins=}")

    if target_remaining == 0:
        """if coins_used < min_coins:""" #Not necessary, as check already handles this case.
        min_coins = coins_used
        min_change = dict(change)
        return False
    
    if index >= len(denoms):
        return False

    cur_denom = denoms[index]

    if coins_used + math.ceil(target_remaining/cur_denom) >= min_coins: #check
        return False


    max_num_cur_denom = target_remaining // cur_denom
    for num_cur_denom in range(max_num_cur_denom, -1, -1):
        change[cur_denom] = num_cur_denom
        cont = make_change_bnb_helper(change, target_remaining - num_cur_denom * cur_denom, denoms, index + 1, coins_used + num_cur_denom)
        change[cur_denom] = 0
        if not cont:
            break

    return True





def make_change_bnb(target, denoms):
    change = {denom: 0 for denom in denoms}
    denoms.sort(reverse=True)
    make_change_bnb_helper(change, target, denoms, 0, 0)

    return min_coins, min_change


def main():
    denoms = list(eval(input("Enter a comma-separated list of coin denominations: ")))
    target = int(input("Enter the target amount to make change for: "))
    min_coins, min_change = make_change_bnb(target, denoms)
    print(f"Minimum number of coins required to make change: {min_coins}")
    print(f"Change: {min_change}")


if __name__ == "__main__":
    main()
